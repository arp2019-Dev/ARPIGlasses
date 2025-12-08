import pygame
import time
import sys
import random

pygame.init()

# ---- Display ----
WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smart Glasses Demo")

# ---- Font ----
time_font = pygame.font.SysFont("Arial", 110, bold=True)
matrix_font = pygame.font.SysFont("Courier", 20, bold=True)

clock = pygame.time.Clock()

# Cycle timing
MODES = ["clock", "ball", "stars", "matrix"]
mode_index = 0
mode_time = time.time()

# ---- Animation State ----
# Bouncing ball
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = 4, 3
ball_size = 50

# Starfield
stars = []
for _ in range(80):
    stars.append([random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(5, 10)])

# Matrix columns
matrix_cols = WIDTH // 20
matrix_drops = [random.randint(-20, HEIGHT) for _ in range(matrix_cols)]

# --------------------------------------------------------------
def rotate_for_glasses(surface):
    """Rotate + flip to match your 90° glasses orientation."""
    rot = pygame.transform.rotate(surface, 90)
    return pygame.transform.flip(rot, True, False)

# --------------------------------------------------------------
def draw_clock():
    current_time = time.strftime("%I:%M %p")

    surf = time_font.render(current_time, True, (255, 255, 255))
    final = rotate_for_glasses(surf)
    rect = final.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(final, rect)

# --------------------------------------------------------------
def draw_ball():
    global ball_x, ball_y, ball_dx, ball_dy

    ball_x += ball_dx
    ball_y += ball_dy

    # Bounce
    if ball_x < ball_size or ball_x > WIDTH - ball_size:
        ball_dx *= -1
    if ball_y < ball_size or ball_y > HEIGHT - ball_size:
        ball_dy *= -1

    ball_surface = pygame.Surface((ball_size*2, ball_size*2), pygame.SRCALPHA)
    pygame.draw.circle(ball_surface, (0, 200, 255), (ball_size, ball_size), ball_size)

    final = rotate_for_glasses(ball_surface)
    screen.blit(final, final.get_rect(center=(ball_x, ball_y)))

# --------------------------------------------------------------
def draw_stars():
    for star in stars:
        x, y, speed = star
        y += speed
        if y > HEIGHT:
            y = 0
            x = random.randint(0, WIDTH)

        star[0], star[1] = x, y
        pygame.draw.rect(screen, (255, 255, 255), (x, y, speed, speed))

    # Apply rotation
    final = rotate_for_glasses(screen.copy())
    screen.blit(final, (0, 0))

# --------------------------------------------------------------
def draw_matrix():
    global matrix_drops

    for i in range(matrix_cols):
        char = chr(random.randint(33, 126))
        surf = matrix_font.render(char, True, (0, 255, 70))
        
        y = matrix_drops[i] * 20
        x = i * 20

        screen.blit(surf, (x, y))

        matrix_drops[i] += 1
        if y > HEIGHT and random.random() > 0.975:
            matrix_drops[i] = random.randint(-20, 0)

    # Rotate entire frame
    final = rotate_for_glasses(screen.copy())
    screen.blit(final, (0, 0))

# --------------------------------------------------------------
while True:

    # --- INPUT ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # --- MODE CYCLING ---
    if time.time() - mode_time > 5:
        mode_index = (mode_index + 1) % len(MODES)
        mode_time = time.time()

    mode = MODES[mode_index]

    # Clear screen
    screen.fill((0, 0, 0))

    # --- DRAW MODE ---
    if mode == "clock":
        draw_clock()

    elif mode == "ball":
        draw_ball()

    elif mode == "stars":
        draw_stars()

    elif mode == "matrix":
        draw_matrix()

    pygame.display.update()
    clock.tick(60)
