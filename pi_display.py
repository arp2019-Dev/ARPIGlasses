import os
import pygame
import asyncio
import json
import websockets
import threading
from queue import Queue

# ---------- SDL / DRM SETUP ----------
os.environ["SDL_VIDEODRIVER"] = "kmsdrm"
os.environ["SDL_AUDIODRIVER"] = "dummy"
os.environ["SDL_NOMOUSE"] = "1"

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
framebuffer = pygame.Surface((width, height))


font_title = pygame.font.SysFont("Arial", 72)
font_content = pygame.font.SysFont("Arial", 48)

# ---------- SHARED STATE ----------
state_queue = Queue()
title_text = "Waiting for iPhone..."
content_text = ""

def render():
    framebuffer.fill((0, 0, 0))

    title = font_title.render(title_text, True, (255, 255, 255))
    content = font_content.render(content_text, True, (255, 255, 255))

    framebuffer.blit(
        title,
        title.get_rect(center=(width // 2, height // 4))
    )
    framebuffer.blit(
        content,
        content.get_rect(center=(width // 2, height // 2))
    )

    # 🔄 Vertical flip
    flipped = pygame.transform.flip(framebuffer, False, True)

    screen.blit(flipped, (0, 0))
    pygame.display.flip()


# ---------- WEBSOCKET SERVER ----------
async def handler(websocket):
    print("📡 iPhone connected")
    async for message in websocket:
        print("📨", message)
        data = json.loads(message)
        state_queue.put(data)

async def start_server():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("🖥️ Display server running")
        await asyncio.Future()

def run_async():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_server())

threading.Thread(target=run_async, daemon=True).start()

# ---------- MAIN LOOP (RENDER THREAD) ----------
try:
    while True:
        pygame.event.pump()

        while not state_queue.empty():
            data = state_queue.get()

            app = data.get("app")
            payload = data.get("payload", {})

            if app == "time":
                title_text = "Time"
                content_text = payload.get("content", "")

            elif app == "weather":
                title_text = "Weather"
                content_text = payload.get("content", "")

            elif app == "text":
                title_text = "Message"
                content_text = payload.get("content", "")

            render()

except KeyboardInterrupt:
    pygame.quit()
