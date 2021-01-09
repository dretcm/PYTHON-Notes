# (1) ------------------------------------ window, rename, size, quit ---------------------------------- #

import pygame, sys
from pygame.locals import *  # for QUIT, etc

clock = pygame.time.Clock()  # for the 'x' fps
WINDOW_SIZE = (400, 400)

pygame.display.set_caption('My Pygame window ')   # set the name of window
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)  # set the size of window

while True:
        
        for event in pygame.event.get():  # events at interact with the display, window.
                if event.type == QUIT:  # QUIT is event type or message of exit or close pygame´s window.
                        pygame.quit() # exit from pygame
                        sys.exit()  # exit from Python
                        
        pygame.display.update()
        clock.tick(60)  # for the 60 fps

# (2) ------------------------------------ window, rename, size, quit ---------------------------------- #
