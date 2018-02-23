# snake game!
import pygame
import sys
import random
import time

check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!) Had {0} initializing errors, exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) Pygame Successfully installed")

# Player surface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake game!!')

# Colors
red = pygame.Color(255, 0, 0) #gameover
green = pygame.Color(0, 255, 0) #snake
black = pygame.Color(0, 0, 0) #score
white = pygame.Color(255, 255, 255) #background
brown = pygame.Color(165, 42, 42) #food

# FPS Controller
fpsController = pygame.time.Clock()

# Important Variables
snakePos =
