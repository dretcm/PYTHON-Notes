# pague of colors in RGB: https://htmlcolorcodes.com/

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
               
# FULLSCREEN and gets:

import pygame

clock = pygame.time.Clock() 
pygame.init()

pygame.display.set_caption('My Pygame Window ')
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

width = pygame.display.get_surface().get_width()  # example 1380
height = pygame.display.get_surface().get_height() # 768

# (2) ----------------------------- load image, fill background, inputs, physics, collisions, draw rect --------------------------- #

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
test_rect = pygame.Rect(100, 100, 100, 50) # Rect(left, top, width, height)

while True:
        screen.fill((146, 244, 255)) # fill background with the colors RGB (0-255)(black-white)
        # screen.fill((0, 0, 0)) # for clear the screen in black
        
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
                # pygame.draw.rect(screen, (0, 0, 0), [pos_x, pos_y, width, height])
		# pygame.draw.rect(screen, (255,0,0), button, 0) # (screen, color RGB, 1:invisible, 0: fill, 1....90:edge bold)

        
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

# draw circle :

pygame.draw.circle(display,(255,255,255),(600,700),40) # screen, color, radius

        
# (3) ------------------------------------ full screen window, audio ---------------------------------- #  
# example of programming hero (Halloween XD).
import pygame
from time import sleep

pygame.init()
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

pygame.mixer.init()
pygame.mixer.music.load('ratsasan.mp3')
pygame.mixer.music.play()

sleep(2)

pygame.mixer.music.load('scary.mp3')

image = pygame.image.load('scr.jpg')
window.blit(image, (0,0))

pygame.mixer.music.play()

pygame.display.update()

sleep(3)

# also we can use for playing after of test.mp3:
pygame.mixer.music.queue("test2.mp3")

# loop music and begin of play:
# by default is '0', that is to say, that it just plays once, -1 for loops.
# "start" is the time in seconds to start, be default is 0, i mean, at the begining of song.
pygame.mixer.music.play(loops=-1, start=35)

# (4) ------------------------------------ transform images, transparent images, text, colliderect  ---------------------------------- # 

import pygame, sys
from pygame.locals import *

clock = pygame.time.Clock()
WINDOW_SIZE = (600, 500)

pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)

width = pygame.display.get_surface().get_width()  # get width of hte window
height = pygame.display.get_surface().get_height() # get height of hte window

bg = pygame.transform.scale(pygame.image.load('bg.png'), (width, height)) # (image, (width, height) to scale)

# apple:
score = 0
apple_img = pygame.transform.scale(pygame.image.load('apple.png'), (25, 25))
apple_img.set_colorkey((255, 255, 255))  # color which will be transparent o equals to background

apple = pygame.Rect(0, 0, 25, 25)
state_apple = True

def print_score(score):
        font = pygame.font.Font(None,20) # font or text set
        message = font.render('score: '+str(score), 1, (0,0,0)) # render(text, The antialias argument is a boolean: if true the characters will have smooth edges, color, background=None) 
        return message

snake = pygame.Rect(100, 30, 25, 25) # Rect(left, top, width, height)

moving_left = False
moving_right = False
moving_up = False
moving_down = False
speed = 5

# apple:
score = 0
apple = pygame.Rect(0, 0, 25, 25)

while (True):
        screen.blit(bg, (0,0))
        screen.blit(print_score(score),(450,10))
        
        if  pygame.Rect.colliderect(snake, apple):
                print('snake and apple are colliderecting.')
                
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

        pygame.display.update()
        clock.tick(60)

# (5) ------------------------------------ flip and rotate img ---------------------------------- # 

img = pygame.image.load('character.png')
img_flip = pygame.transform.flip(img, boolx,booly) # 1 boolx: horizontal flip; booly: vertical flip ;2 boolx and booly: horizontal and vertical flip

angle = 180 # also can be 0,90,270, etc.
img_rotate = pygame.transform.rotate(img, angle)


# (6) ------------------------------------ button, mouse ---------------------------------- # 

font = pygame.font.Font(None,70)

button = pygame.Rect(150,300, 250,70)
pygame.draw.rect(screen, (255,100,0), button)

message = font.render('Play',1,(0,0,0))
screen.blit(message, (160,310))
                        
pygame.display.update()
                        
for event in pygame.event.get():
        if event.type == QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and button.collidepoint(event.pos):
                        print('you clicked the button')



## mouse:

import pygame, sys
from pygame.locals import *

clock = pygame.time.Clock() 
pygame.init()


WINDOW_SIZE = (600,400)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32)

#help(pygame.mouse) # more abourt mouse in pygame

font = pygame.font.Font(None,20)

while True:
        screen.fill((146, 244, 255))

        message = font.render(str(pygame.mouse.get_pos()), 1, (0,0,0))  # get positon of mouse
        screen.blit(message,(10,10))
        
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit() 
                        sys.exit()
                        
        pygame.display.update()
        clock.tick(30)
                        
# (7) ------------------------------------ surface, center of image ---------------------------------- #

# example 1:

import pygame, sys
from pygame.locals import *

clock = pygame.time.Clock() 
pygame.init()


WINDOW_SIZE = (600,400)
screen = pygame.display.set_mode(WINDOW_SIZE,0,32)

display = pygame.Surface((1200, 800))  # creata a plane or superfice in (width,height) = 1200, 800

font = pygame.font.Font(None,100)

img_ball = pygame.transform.scale(pygame.image.load('ball.png'), (100, 100))  # image 100x100px
img_ball.set_colorkey((255, 255, 255))

while True:
        display.fill((146, 244, 255))  # use surface not screen

        message = font.render(str(pygame.mouse.get_pos()), 1, (0,0,0))
        display.blit(message,(800,60)) # use surface
        
        x,y = pygame.mouse.get_pos()
        display.blit(img_ball, (x*2-50,y*2-50))   # midle of image or center of image the form is: center = tuple(width_img/2,heigt/2), in this case the center is 50,50 in an img of 100x100px
        
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit() 
                        sys.exit()
                        
        surf = pygame.transform.scale(display, WINDOW_SIZE)  # resize the surface of (1200,800) to (600,400)
        screen.blit(surf, (0, 0))  # now, show the surface in the screen in the position 0,0 for doing a simulation of that the surface is the screen.
        pygame.display.update()  # update all frames and goo
        clock.tick(30)

# (8) ------------------------------------ dialog player, camera ---------------------------------- #
# (9) ------------------------------------ input text  ---------------------------------- #

# example 1:

def main():
    screen = pg.display.set_mode((640, 480))
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(100, 100, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()


# example 2: 

class InputText:
        font = pygame.font.Font(None, 32)
        input_box = pygame.Rect(0, 0, 140, 40)
        color_inactive = pygame.Color((0,255,0))
        color_active = pygame.Color((255,0,0))
        color = color_inactive
        active = False
        text = ''
        
        def set_mouse(self, pos):
                if self.input_box.collidepoint(pos):
                        self.active = not self.active
                else:
                        self.active = False
                self.color = self.color_active if self.active else self.color_inactive

        def set_keyboard(self,event):
                if self.active:
                        if event.key == K_RETURN:
                                print(self.text)
                                self.text = ''
                        elif event.key == K_BACKSPACE:
                                self.text = self.text[:-1]
                        else:
                                self.text += event.unicode
                                        
        def run_input(self, display):                              
                txt_surface = self.font.render(self.text, True, self.color)
                width = max(200, txt_surface.get_width()+10)
                self.input_box.w = width
                display.blit(txt_surface, (self.input_box.x+5, self.input_box.y+5))
                pygame.draw.rect(display, self.color, self.input_box, 2)


# in the while and for to events:

                if event.type == MOUSEBUTTONDOWN:
                        entry.set_mouse(event.pos)
                if event.type == KEYDOWN:
                        if event.key == K_LEFT:
                                move_left = True
                        if event.key == K_RIGHT:
                                move_right = True
                        if event.key == K_UP:
                                move_up = True
                        if event.key == K_DOWN:
                                move_down = True
                        entry.set_keyboard(event)

# example 3:

class InputText:
        font = pygame.font.Font(None, 35)
        input_box = [500, 350, 140, 40]
        color = pygame.Color((0,255,0))
        text = ''

        def set_keyboard(self,event):
                if event.key == K_RETURN:
                        print(self.text)
                        self.text = ''
                elif event.key == K_BACKSPACE:
                        self.text = self.text[:-1]
                else:
                        self.text += event.unicode
                                        
        def run_input(self, display):                             
                txt_surface = self.font.render(self.text, True, self.color)
                
                width = max(200, txt_surface.get_width()+10)
                self.input_box[2] = width
                
                x,y = self.input_box[0], self.input_box[1]

                display.blit(txt_surface, (x+5, y+10))
                pygame.draw.rect(display, self.color, self.input_box, 2)


# (10) ------------------------------------ input text  ---------------------------------- #
# (11) ------------------------------------ input text  ---------------------------------- #
# (12) ------------------------------------ input text  ---------------------------------- #
# (13) ------------------------------------ input text  ---------------------------------- #
# (14) ------------------------------------ input text  ---------------------------------- #
# (15) ------------------------------------ input text  ---------------------------------- #
# (16) ------------------------------------ input text  ---------------------------------- #
# (17) ------------------------------------ input text  ---------------------------------- #
