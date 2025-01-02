import pygame
from pygame.locals import *

pygame.init()

# Setting screen size
pixel_size = 32
screen_width = 30*pixel_size
screen_height = 16*pixel_size
display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Simulation Example')  

# Main Loop
running = True
while running:
    for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            pygame.quit()
            running = False
            break
        
        elif e.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            pygame.draw.circle(display, (255, 255, 255), pygame.mouse.get_pos(), pixel_size//2)
            
        elif e.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]:
            pygame.display.flip()
            display.fill((0, 0, 0))

        
