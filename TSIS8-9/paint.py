import pygame
import sys

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Drawing Program")

# Load eraser image
eraser_img = pygame.image.load("eraser.jpg")

# Scale eraser image
eraser_img = pygame.transform.scale(eraser_img, (30, 30))

# Variables for drawing control
drawing = False
last_pos = None
color = BLACK
radius = 5

# Create surface to store drawing
drawing_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
drawing_surface.fill(WHITE)

# Main program loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                drawing = True
                last_pos = event.pos
            elif event.button == 3:  # Right mouse button
                color = WHITE
            elif event.button == 2:  # Middle mouse button (scroll wheel)
                color = BLACK
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                drawing = False
                last_pos = None
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                new_pos = event.pos
                pygame.draw.line(drawing_surface, color, last_pos, new_pos, radius*2)
                last_pos = new_pos
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:  # Press "e" key to clear screen
                drawing_surface.fill(WHITE)

    # Display drawing on screen
    screen.blit(drawing_surface, (0, 0))

    # Draw color palette
    pygame.draw.rect(screen, RED, (10, 10, 30, 30))
    pygame.draw.rect(screen, GREEN, (50, 10, 30, 30))
    pygame.draw.rect(screen, BLUE, (90, 10, 30, 30))

    # Display eraser as a button
    screen.blit(eraser_img, (130, 10))

    # User interaction handling
    mouse_pos = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        if 10 <= mouse_pos[0] <= 40 and 10 <= mouse_pos[1] <= 40:
            color = RED
        elif 50 <= mouse_pos[0] <= 80 and 10 <= mouse_pos[1] <= 40:
            color = GREEN
        elif 90 <= mouse_pos[0] <= 120 and 10 <= mouse_pos[1] <= 40:
            color = BLUE
        elif 130 <= mouse_pos[0] <= 160 and 10 <= mouse_pos[1] <= 40:
            color = WHITE

    # Delay for screen update
    pygame.time.delay(30)

    # Update screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
