# Pygame Simulations
Hello! This project is a quick demo for presentation that I'll be doing in the Michigan Python group in Jan 2th 2025.
In this project you have:
## setup.py 
- It's a blank script that just creates the screen. You can build your application on top of it by just adding more events/drawings on screen

## example1.py
- This script show you how to draw graphical elements on screen. To do that you can use commands such as any of the `pygame.draw` methods or `display.blit` and update the screen with `pygame.display.flip`
- In this example I'm using `pygame.draw.circle` to draw some circles
- When you left click on the screen, a white circle is drawn where you clicked
- To make the circles show you can use the right click, as that is going to run `pygame.display.flip` and update what is currently shown on the screen

## example2.py
- This script shows how you can start making the simulations dynamic by adding motion to the ball
- The approach used here is to incrementaly update the circle speed and position
- Each new frame has a slight increment to those values such that it makes the ball fall, simulating gravity
- On this example there's no collision handling, so the ball just falls out of the screen

## example3.py
- This exaple is the most complete one. It deals with collision handling so that the ball is always on screen and uses real-life physics formulas to calculate the position
- You can also customize a lot of the simulation by changing the parameters on the top of the code
- The simulation calculates the movement by having 2 motion axis that are calculated independently
  - The horizontal motion is simply based on the initial value, as there's no horizontal acceleration
  - The vertical motion is calculated based on the initial value and gravity acceleration
  - When a collision with the ground is detected, the velocity values are updated based on the elasticity coefficient
  - When the ball gets on the side margin of the screen it is simply moved to the other side

# How to run the project
- (Optional) Setup a virtual environment with the command `python -m venv sim`
  - You can name it however you like but the name `sim` is already present in the gitignore, so it will be easier
- Install pygame with the command `pip install pygame`
  - Make sure to activate the virtual environment if you are using it

## And that's all, you should be ready to run the project
## Make sure to look for the other repositories on my profile!
