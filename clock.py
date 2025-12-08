import pygame
import time
import sys

# Initialize Pygame
pygame.init()

# Set video mode for composite output (Pi config decides actual resolution)
WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Rotated Clock")

# Font setup
font = pygame.font.SysFont("Arial", 120, bold=True)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get current time
    current_time = time.strftime("%H:%M:%S")

    # Render text
    text_surface = font.render(current_time, True, (255, 255, 255))

    # Make a black background
    screen.fill((0, 0, 0))

    # Rotate by 90 degrees
    rotated = pygame.transform.rotate(text_surface, 90)

    # Flip horizontally + vertically depending on your display
    flipped = pygame.transform.flip(rotated, True, False)

    # Center it
    rect = flipped.get_rect(center=(WIDTH//2, HEIGHT//2))

    # Draw
    screen.blit(flipped, rect)

    pygame.display.update()
    clock.tick(1)   # Update every second
