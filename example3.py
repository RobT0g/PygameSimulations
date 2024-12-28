import pygame
from pygame.locals import *
import math

pygame.init()

# Starting Position, Speed and Gravity
starting_pos = [300, 200]
starting_speed = [5, -10]
gravity_accel = 10
ground_level = 32

# Setting screen size
pixel_size = 32
screen_width = 40*pixel_size
screen_height = 30*pixel_size
display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Simulation Example')  

# Creating Screen Frame
frame = pygame.Surface((screen_width, screen_height))
frame.fill((20, 50, 150))
ground_level = screen_height - ground_level
pygame.draw.rect(frame, (0, 255, 0), (0, ground_level, screen_width, pixel_size))

# Setting refresh rate
refresh = 25
timeStep = 150
clock = pygame.time.Clock() 
update = pygame.USEREVENT + 1
pygame.time.set_timer(update, refresh)

# Creating ball
ball = pygame.Surface((pixel_size, pixel_size), pygame.SRCALPHA)
pygame.draw.circle(ball, (255, 255, 255), (pixel_size//2, pixel_size//2), pixel_size//2)

# Formula Values
space_initial = starting_pos[:]
velocity_initial = starting_speed[:]
current_pos = starting_pos[:]
current_speed = starting_speed[:]
current_time = 0
time_modifier = [0, 0]

# Pause Variable
paused = True

def update_variables():
    global current_pos, current_time, speed, paused

    if paused:
        return

    # Incrementing time
    current_time += timeStep
    formula_time = [(current_time - i)/1000 for i in time_modifier]
    if current_time/1000 >= 12.84: paused = True

    # Updating ball position
    current_pos[0] = space_initial[0] + velocity_initial[0]*formula_time[0]
    current_pos[1] = space_initial[1] + velocity_initial[1]*formula_time[1] + (gravity_accel*(formula_time[1]**2))/2

    # Updating speed values
    current_speed[1] = velocity_initial[1] + gravity_accel*formula_time[1]

def check_collision_at_y_axis():
    # if current_pos[1] + ball.get_size()[1] < ground_level:
    #     return
    
    delta = (4*velocity_initial[1]**2) - 4 * gravity_accel * (2*space_initial[1] - 2*ground_level + 2*ball.get_size()[1])
    collision_time = (-2*velocity_initial[1] + math.sqrt(delta))/(2*gravity_accel)
    print(collision_time)

    # velocity_initial[1] = -0.85 * velocity_initial[1]
    # if abs(velocity_initial[1]) < 1: 
    #     velocity_initial[1] = 0

check_collision_at_y_axis()

# Main Loop
running = True
while running:
    for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            pygame.quit()
            running = False
            break

        elif e.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            current_pos = starting_pos[:]
            current_time = 0
            speed = starting_speed[:]
            paused = not paused

        elif e.type == update:
            display.blit(frame, (0, 0))
            display.blit(ball, current_pos)
            pygame.display.flip()
            
            update_variables()
            #check_collision()

