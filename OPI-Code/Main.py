import asyncio, pygame, threading, json, cv2, time, psutil
from aiohttp import web
from smbus2 import SMBus
from math import atan2, sqrt

WIDTH, HEIGHT = 640, 480
MPU_ADDR = 0x68
FPS = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("Courier", 20)
clock = pygame.time.Clock()
bus = SMBus(1)
bus.write_byte_data(MPU_ADDR, 0x6B, 0) 

bounding_boxes, overlay_mode, voice_text, annotations = [], "detection", "", []
pose_data = {"pitch": 0, "yaw": 0}
last_fps_time, fps_count, current_fps = time.time(), 0, 0

def get_mpu_data():
    def r(reg): return (bus.read_byte_data(MPU_ADDR, reg) << 8) + bus.read_byte_data(MPU_ADDR, reg + 1)
    ax, ay, az = r(0x3B), r(0x3D), r(0x3F)
    gx, gy, gz = r(0x43), r(0x45), r(0x47)
    ax, ay, az = (ax - 65536 if ax > 32768 else ax)/16384.0, (ay - 65536 if ay > 32768 else ay)/16384.0, (az - 65536 if az > 32768 else az)/16384.0
    return ax, ay, az, gx / 131.0, gy / 131.0, gz / 131.0

def draw_loop():
    global fps_count, current_fps
    while True:
        screen.fill((0, 0, 0))

        ax, ay, az, gx, gy, gz = get_mpu_data()
        imu = f"A: {ax:.2f} {ay:.2f} {az:.2f} G: {gx:.2f} {gy:.2f} {gz:.2f}"
        screen.blit(font.render(imu, True, (255, 255, 0)), (10, 10))

        screen.blit(font.render(f"Pose: P{pose_data['pitch']:.1f} Y{pose_data['yaw']:.1f}", True, (150, 255, 255)), (10, 35))

        screen.blit(font.render(f"Say: {voice_text}", True, (255, 255, 255)), (10, HEIGHT - 60))

        screen.blit(font.render(f"Mode: {overlay_mode}", True, (255, 100, 100)), (WIDTH - 160, 10))

        fps_count += 1
        if time.time() - last_fps_time > 1:
            current_fps = fps_count
            fps_count = 0
        screen.blit(font.render(f"FPS: {current_fps}", True, (255, 255, 255)), (WIDTH - 160, 35))

        if overlay_mode == "detection":
            for x, y, w, h, label in bounding_boxes:
                pygame.draw.rect(screen, (0, 255, 0), (x, y, w, h), 2)
                screen.blit(font.render(label, True, (0, 255, 0)), (x, y - 20))

        for note in annotations:
            x, y, text = note
            pygame.draw.circle(screen, (255, 0, 255), (x, y), 5)
            screen.blit(font.render(text, True, (255, 0, 255)), (x + 5, y))

        pygame.display.flip()
        clock.tick(FPS)

async def handle_ws(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    global bounding_boxes, overlay_mode, voice_text, pose_data, annotations

    async for msg in ws:
        if msg.type == web.WSMsgType.TEXT:
            data = json.loads(msg.data)
            if "boxes" in data: bounding_boxes = data["boxes"]
            if "voice" in data: voice_text = data["voice"]
            if "pose" in data: pose_data = data["pose"]
            if "mode" in data: overlay_mode = data["mode"]
            if "annotate" in data: annotations.append(data["annotate"])
    return ws

if __name__ == "__main__":
    threading.Thread(target=draw_loop, daemon=True).start()
    app = web.Application()
    app.router.add_get('/ws', handle_ws)
    web.run_app(app, port=8765)
