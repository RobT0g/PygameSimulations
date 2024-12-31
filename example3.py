import pygame
from pygame.locals import *
import math

pygame.init()

# Customizable Parameters
starting_pos = [200, 500]
starting_speed = [-40, -40]
gravity_accel = 10
ground_level = 32
timeStep = 200
elasticity_coeficient = 10
circle_radius = 16
show_arrows = True
arrow_size = 2

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
time_modifier = 0
collision_time = 0

# Pause Variable
paused = True

def update_variables():
    global current_pos, current_time, current_pos, current_speed, space_initial, velocity_initial, paused, time_modifier, collision_time

    if paused:
        return

    # Incrementing time
    current_time += timeStep
    formula_time = (current_time - time_modifier)/1000

    # Checking collisions
    if formula_time >= collision_time and collision_time >= 0.5:
        #print('Collided!')
        time_modifier = time_modifier + collision_time*1000
        formula_time = (current_time - time_modifier)/1000

        space_initial[0] = space_initial[0] + velocity_initial[0]*collision_time
        velocity_initial[0] = (1-elasticity_coeficient/100) * velocity_initial[0]

        space_initial[1] = ground_level-circle_radius
        velocity_initial[1] = (-1+elasticity_coeficient/100)*(velocity_initial[1] + gravity_accel*collision_time)

    # Updating ball position and speed
    if collision_time <= 0.5:
        current_pos[1] = ground_level-circle_radius
        current_speed = [0, 0]
    else:
        current_pos[1] = space_initial[1] + velocity_initial[1]*formula_time + (gravity_accel*(formula_time**2))/2
        current_pos[0] = (space_initial[0] + velocity_initial[0]*formula_time)%screen_width
        current_speed[0] = velocity_initial[0]
        current_speed[1] = velocity_initial[1] + gravity_accel*formula_time
    
    check_collision_at_y_axis()

def check_collision_at_y_axis():
    global space_initial, velocity_initial, paused, time_modifier, collision_time

    delta = (4*velocity_initial[1]**2) - 4 * gravity_accel * (2*space_initial[1] - 2*ground_level + 2*circle_radius)
    collision_time = (-2*velocity_initial[1] + math.sqrt(delta))/(2*gravity_accel)

    #print(collision_time)

# Calculate initial collision
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
            #display.blit(ball, current_pos)
            pygame.draw.circle(display, (255, 255, 255), current_pos, pixel_size//2)
            if show_arrows:
                pygame.draw.line(display, (0, 100, 0), current_pos, (current_pos[0]+current_speed[0]*arrow_size, current_pos[1]), 3)
                pygame.draw.line(display, (0, 100, 0), current_pos, (current_pos[0], current_pos[1]+current_speed[1]*arrow_size), 3)
            pygame.display.flip()
            
            update_variables()

