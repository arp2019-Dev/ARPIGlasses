import pygame
import time
import sys

pygame.init()

# Keep your display settings exactly the same
WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smart Glasses Clock")

# Font
time_font = pygame.font.SysFont("Arial", 110, bold=True)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # ---- TIME (12-hour, no seconds) ----
    current_time = time.strftime("%I:%M %p")

    # Render time
    time_surface = time_font.render(current_time, True, (255, 255, 255))

    # Clear screen (black)
    screen.fill((0, 0, 0))

    # Rotate display 90 degrees (your setup)
    time_rot = pygame.transform.rotate(time_surface, 90)

    # Flip to match your glasses orientation
    time_final = pygame.transform.flip(time_rot, True, False)

    # Center the time
    time_rect = time_final.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    # Draw
    screen.blit(time_final, time_rect)

    pygame.display.update()
    clock.tick(1)
