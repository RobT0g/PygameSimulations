import pygame
from pygame.locals import *

pygame.init()

# Starting Position and Speed
starting_pos = 200
starting_speed = -30

# Setting screen size
pixel_size = 32
screen_width = 16*pixel_size
screen_height = 30*pixel_size
display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Simulation Example')  

# Creating Screen Frame
frame = pygame.Surface((screen_width, screen_height))
frame.fill((20, 50, 150))
ground_level = screen_height - pixel_size
pygame.draw.rect(frame, (0, 255, 0), (0, ground_level, screen_width, pixel_size))

# Setting refresh rate
refresh = 50
timeStep = 100
clock = pygame.time.Clock() 
update = pygame.USEREVENT + 1
pygame.time.set_timer(update, refresh)

# Creating ball
ball = pygame.Surface((pixel_size, pixel_size), pygame.SRCALPHA)
pygame.draw.circle(ball, (255, 255, 255), (pixel_size//2, pixel_size//2), pixel_size//2)
current_pos = starting_pos
speed = starting_speed

# Creating Gravity
gravity_accel = 10 # m/s^2

# Pause Variable
paused = True

def update_variables():
    global current_pos, speed, paused
    if paused:
        return
    
    # Updating ball position
    current_pos += speed
    
    # Updating speed
    speed += gravity_accel*timeStep/1000

# Main Loop
running = True
while running:
    for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            pygame.quit()
            running = False
            break

        elif e.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            current_pos = starting_pos
            speed = starting_speed
            paused = not paused

        elif e.type == update:
            display.blit(frame, (0, 0))
            display.blit(ball, [(screen_width//2) - (pixel_size//2), current_pos])
            pygame.display.flip()
            
            update_variables()

