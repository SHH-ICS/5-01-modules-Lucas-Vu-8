# Using the pygame library, draw a simple picture. 
# It can be anything you like, but you must use at least 2 different types of shapes and 3 different colors.

#https://replit.com/@Lucasvu3/ImpracticalExperiencedJavadoc
import pygame
import sys

# Initialize pygame
pygame.init()

# Set up display
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Picture")

# Colors
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Main loop
running = True
while running:
    # Fill the background
    screen.fill(WHITE)

    # Draw shapes
    # Draw a blue rectangle
    pygame.draw.rect(screen, BLUE, (50, 50, 100, 60))

    # Draw a green circle
    pygame.draw.circle(screen, GREEN, (200, 150), 50)

    # Draw a red triangle
    pygame.draw.polygon(screen, RED, [(300, 300), (350, 250), (400, 300)])

    # Update the display
    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit pygame
pygame.quit()
sys.exit()
