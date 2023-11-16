import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the window
width, height = 800, 800
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Death Star")

# Colors
black = (0, 0, 0)
gray = (100, 100, 100)
white = (255, 255, 255)

# Function to draw the Death Star
def draw_death_star():
    # Clear the window
    window.fill(black)
    
    # Draw the Death Star - a simple representation using circles and lines
    pygame.draw.circle(window, gray, (width//2, height//2), 300)
    pygame.draw.circle(window, black, (width//2, height//2), 250)
    
    # Draw details
    pygame.draw.circle(window, gray, (width//2, height//2 - 50), 30)
    pygame.draw.circle(window, gray, (width//2 - 100, height//2 - 100), 40)
    pygame.draw.circle(window, gray, (width//2 + 100, height//2 - 100), 40)
    
    pygame.draw.line(window, gray, (width//2 - 150, height//2), (width//2 - 180, height//2 - 100), 5)
    pygame.draw.line(window, gray, (width//2 + 150, height//2), (width//2 + 180, height//2 - 100), 5)
    
    # Update the display
    pygame.display.update()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    draw_death_star()

# Quit Pygame
pygame.quit()
