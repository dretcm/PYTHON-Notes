# (1) ----------------------------------------- window, rename, size, quit --------------------------------------------- #

import pygame, sys
from pygame.locals import *  # for QUIT, etc

clock = pygame.time.Clock()  # for the 'x' fps
WINDOW_SIZE = (400, 400)

pygame.init() # initial pygame

pygame.display.set_caption('My Pygame window ')   # set window´s name
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)  # set the size of window, or initial the screen

while True:
        
        for event in pygame.event.get():  # events at interact with the display, window, screen.
                if event.type == QUIT:  # QUIT is event type or message of exit or close pygame´s window.
                        pygame.quit() # exit from pygame
                        sys.exit()  # exit from Python
                        
        pygame.display.update() # makes that display update according above process
        clock.tick(60)  # for the 60 fps

# (2) ----------------------------- load image, fill background, inputs, physics, collisions --------------------------- #

import pygame, sys
from pygame.locals import *

clock = pygame.time.Clock() 
WINDOW_SIZE = (400, 400)

pygame.init()

pygame.display.set_caption('My Pygame Window ')
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32) 

player_image = pygame.image.load('character.png')   # import, open image

player_location = [0, 0] # [X, Y]
player_y_momentum = 0.0 # weight

moving_left = False  # States of keyboard
moving_right = False

speed = 4  # horizontal speed of character

player_rect  = pygame.Rect(player_location[0], player_location[1], player_image.get_width(), player_image.get_height()) # rectangular collider with size of player
test_rect = pygame.Rect(100, 100, 100, 50) # rectangular collider with size test

while True:
        screen.fill((146, 244, 255)) # fill background with the colors RGB (0-255)
        
        screen.blit(player_image, player_location) # put the image in the surface (image loaded, image´s position)
        # the axis(X,Y) is inverted.
        # where (0,0) is TOP-LEFT and (400,400) is BOTTON-RIGHT.

        if player_location[1] > WINDOW_SIZE[1] - player_image.get_height(): # PHYSICS, GRAVITY
                player_y_momentum = - player_y_momentum    # reverse
        else:
                player_y_momentum += 0.2
        player_location[1] += player_y_momentum   # player_location update according the momentum
        
        if moving_left ==  True:
                player_location[0] -= speed
        if moving_right ==  True:
                player_location[0] += speed

        player_rect.x = player_location[0]  # player collider update according player´s position(x,y)
        player_rect.y = player_location[1]

        if player_rect.colliderect(test_rect):    # function of collison
                pygame.draw.rect(screen, (255, 0, 0), test_rect)   # draw a rectangle in "screen", with the color "255,0,0 (Red)", and his collider is "test_rect".
        else:
                pygame.draw.rect(screen, (0, 0, 0), test_rect)

        
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit() 
                        sys.exit()
                if event.type == KEYDOWN:  # if the key is press, push, etc.
                        if event.key == K_LEFT:
                                moving_left = True
                        if event.key == K_RIGHT:
                                moving_right = True
                if event.type == KEYUP:   # if the key isn´t press, push, etc.
                        if event.key == K_LEFT:
                                moving_left = False
                        if event.key == K_RIGHT:
                                moving_right = False
                        
        pygame.display.update()  # this function will apply the display resfresh
        clock.tick(60)

player_image = pygame.image.load('character.png')  # import, open image

while True:

        screen.blit(player_image, (0, 0))  # put the image in the surface (image loaded, image´s position)
        # the axis(X,Y) is inverted.
        # where (0,0) is TOP-LEFT and (400,400) is BOTTON-RIGHT.
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit() 
                        sys.exit() 
                        
        pygame.display.update() # this function will apply the display resfresh
        clock.tick(60)
        
 
# (3) ------------------------------------ window, rename, size, quit ---------------------------------- #       
# (4) ------------------------------------ window, rename, size, quit ---------------------------------- # 
