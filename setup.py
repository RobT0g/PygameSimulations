import pygame
from pygame.locals import *

# Initialization
pygame.init()

# Setting screen size
screen_width = 400
screen_height = 300
display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Simulation Example')

# Main Loop
running = True
while running:
    for e in pygame.event.get():
        e:pygame.event
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            pygame.quit()
            running = False
            break
            
        if e.type == KEYDOWN and e.key == K_a:
            print('A was pressed')
