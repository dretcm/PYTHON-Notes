# pague of colors in RGB: https://htmlcolorcodes.com/

# (1) ----------------------------------------- window, rename, size, quit --------------------------------------------- #

import pygame, sys
from pygame.locals import *  # for QUIT, etc

clock = pygame.time.Clock()  # for the 'x' fps
WINDOW_SIZE = (400, 400)

pygame.init() # initial pygame

pygame.display.set_caption('My Pygame window ')   # set window´s name or title of the window.
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

        
# (3) ------------------------------------ full screen window, load audio , Sound ---------------------------------- #  
# example of programming hero (Halloween XD).
import pygame
from time import sleep

pygame.init()
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

WINDOW_SIZE = pygame.display.get_window_size()

pygame.mixer.init()
pygame.mixer.music.load('ratsasan.mp3')
pygame.mixer.music.play()

pygame.mixer.music.set_volume(0.2)

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


# stop:
pygame.mixer.music.stop()  # finish the music.

# if put the next line od code, it will continue since the begin.
pygame.mixer.music.play()


# music and difference with sounds : mixer Sound :

https://programmerclick.com/article/704172167/

import pygame, sys

pygame.init()
pygame.mixer.init()

display = pygame.display.set_mode((500, 200))

sound = pygame.mixer.Sound("A.wav")  # create object Sound of mixer.
sound.set_volume(1) # volume of 0% = 0 and 0.5 = 50% and 100% = 1

while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit() 
                        sys.exit()
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                                sound.play()  # play the sound object.
				# sound.stop()
                                
        pygame.display.update()


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
# https://www.remove.bg/upload for remove bg

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

if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 4:  # the slide of wheel mouse. # front
                pass 
        if event.button == 5:  # back

                        
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


# button avance with yes and no :

        def push_button(self, text ='nothing'):

                font = pygame.font.Font(None,70)
                on = False

                midle_x, midle_y = list(map(lambda x: x//2, self.WINDOW_SIZE))

                pos_yes = (midle_x-110, midle_y+50)
                yes = pygame.Rect(pos_yes[0], pos_yes[1], 100,70)
                message_yes = font.render('Yes', 1, (0,0,0))

                pos_no = (midle_x+20, midle_y+50)
                no = pygame.Rect(pos_no[0], pos_no[1], 100,70)
                message_no = font.render('No', 1, (0,0,0))

                pos_msg = (midle_x-150,midle_y-40)
                message = font.render(text,1,(0,0,0))

                self.screen.fill((0,0,0))

                while True:
                        for event in pygame.event.get():
                                if event.type == QUIT:
                                        self.exit_game()
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        if event.button == 1 and yes.collidepoint(event.pos):
                                                print('you clicked the button yes')
                                                on = True
                                                return on
                                                
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        if event.button == 1 and no.collidepoint(event.pos):
                                                print('you clicked the button no')
                                                return on
                                                
                        pygame.draw.rect(self.screen, (255,100,0), yes)
                        self.screen.blit(message_yes, pos_yes)
                        
                        pygame.draw.rect(self.screen, (255,100,0), no)
                        self.screen.blit(message_no, pos_no)
                        
                        pygame.draw.rect(self.screen, (255,255,255), [pos_msg[0], pos_msg[1],300, 60])
                        self.screen.blit(message, pos_msg)
                        
                        pygame.display.update()
                        self.clock.tick(30)
                        
        def exit_game(self):
                pygame.quit()
                sys.exit()

                        
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


# (10) ------------------------------------ dialog in current game  ---------------------------------- #
# class dialog :

class Dialog:
        def __init__(self):
                self.font = pygame.font.Font(None,40)
                self.begin = time.time()
                self.pos = 0
                self.pos_list = 0
                
                self.fast = 0.2
                self.guion = None
                
        def reset(self):
                self.begin = time.time()
                self.pos = 0
                self.pos_list += 1
                
        def text(self):
                now = time.time()
                if now - self.begin > self.fast:
                        self.pos += 1
                        self.begin = now
                if self.pos >= len(self.guion[self.pos_list]) + 3:
                        self.reset()
                msg = self.font.render(self.guion[self.pos_list][:self.pos], 1, (255,255,255))
                return msg

        def message(self, guion):
                self.guion = guion + ['']  # limit of messages
                self.pos_list = 0

        def state(self):
                if self.guion[self.pos_list] == '':
                        return False
                return True

# (11) ------------------------------------ input text, draw line ---------------------------------- #

# pc : input :

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
                txt = self.font.render('PASSWORD', True, self.color)
                txt_surface = self.font.render(self.text, True, self.color)
                
                width = max(200, txt_surface.get_width()+10)
                self.input_box[2] = width
                
                x,y = self.input_box[0], self.input_box[1]
                
                display.blit(txt, (x, y-40))
                display.blit(txt_surface, (x+5, y+5))
                pygame.draw.rect(display, self.color, self.input_box, 2) 
                pygame.draw.rect(display, self.color, (x - 20 , y-60,240, 130), 2)


# draw line with start pos and end pos :
	# aaline(surface, color, start_pos, end_pos)

	pygame.draw.aaline(screen, light_grey, (screen_width/2,0),(screen_width/2,screen_height))

# or:
        x,y = pygame.mouse.get_pos()
        pygame.draw.aaline(screen, light_grey, (screen_width/2,screen_height/2),(x,y))

# (12) ------------------------------------ model of character, player model, sprite ---------------------------------- #

import pygame, sys, time, os
from pygame.locals import *

clock = pygame.time.Clock()
pygame.init()

WINDOW_SIZE = (1200,600)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32)
display = pygame.Surface((1200, 1200))

# character options:
class Player:
        x, y = 600, 700
        speed = 5

        left = False
        right = False
        up = False
        down = False

        can_move = True

        player_collider = pygame.Rect(x,y,40,40)
        
        def down_key(self,key):
                if key == K_LEFT:
                        self.left = True
                if key == K_RIGHT:
                        self.right = True
                if key == K_UP:
                        self.up = True
                if key == K_DOWN:
                        self.down = True
                        
        def up_key(self,key):
                if key == K_LEFT:
                        self.left = False
                if key == K_RIGHT:
                        self.right = False
                if key == K_UP:
                        self.up = False
                if key == K_DOWN:
                        self.down = False
                        
        def moving_player(self, display):
                if self.can_move:
                        x,y = self.get_position()
                        if self.left:
                                x -= self.speed
                        if self.right:
                                x += self.speed
                        if self.up:
                                y -= self.speed
                        if self.down:
                                y += self.speed
                                
                        self.set_position(x,y)
                pygame.draw.rect(display,(255,255,255),self.player_collider)

        def set_move(self, flag):
                self.can_move = flag
                
        def get_position(self):
                return (self.player_collider.x, self.player_collider.y)
        
        def set_position(self,x,y):
                self.player_collider.x = x
                self.player_collider.y = y
                
        def get_collider(self):
                return self.player_collider
        
player = Player()

while True:
        display.fill((0, 0, 0))

        player.moving_player(display)

        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit() 
                        sys.exit()
                if event.type == KEYDOWN:
                        player.down_key(event.key)
                        
                if event.type == KEYUP:
                        player.up_key(event.key)
                        
        surf = pygame.transform.scale(display, WINDOW_SIZE)
        screen.blit(surf, (0, 0))
        
        pygame.display.update()
        clock.tick(30)


# option 2:

# player:
class Player:
        live = True
        speed = 15

        left = False
        right = False
        up = False
        down = False

        width = 80
        height = 80

        sonido_f = pygame.mixer.Sound("music/muerte.mp3")

        speed_sprite = 0.25

        def __init__(self, window_size):
                self.x = window_size[0]//2 - 45
                self.y = window_size[1]//2 - 25
                
                self.rect = pygame.Rect(self.x,self.y, self.width, self.height)

                self.images = []
                for img in ['images/player/p10.png', 'images/player/p11.png', 'images/player/p12.png']:
                        self.images.append(pygame.image.load(img))
                        
                self.actual = 0
                self.image = self.images[self.actual]
        
        def down_key(self,key):
                if key == K_a:
                        self.left = True
                if key == K_d:
                        self.right = True
                if key == K_w:
                        self.up = True
                if key == K_s:
                        self.down = True
                        
        def up_key(self,key):
                if key == K_a:
                        self.left = False
                if key == K_d:
                        self.right = False
                if key == K_w:
                        self.up = False
                if key == K_s:
                        self.down = False
                        
        def moving_player(self, screen):
                
                if self.left:
                        self.rect.x -= self.speed
                if self.right:
                        self.rect.x += self.speed
                if self.up:
                        self.rect.y -= self.speed
                if self.down:
                        self.rect.y += self.speed
                
                screen.blit(self.image, self.get_position())
                
                if self.actual >= len(self.images):
                        self.actual = 0
                self.image = self.images[int(self.actual)]
                self.actual += self.speed_sprite
                
        def get_position(self):
                return (self.rect.x, self.rect.y)
        
        def set_position(self,x,y):
                self.rect.topleft = [x, y]
##                self.rect.x = x
##                self.rect.y = y
                
        def get_collider(self):
                return self.rect

        def set_player_live(self, live):
                self.live = live
                self.sonido_f.play()
                
        def player_live(self):
                return self.live



# sprite examples :

import pygame, sys

class Player(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.attack_animation = False
		self.sprites = []
		self.sprites.append(pygame.image.load('attack_1.png'))
		self.sprites.append(pygame.image.load('attack_2.png'))
		self.sprites.append(pygame.image.load('attack_3.png'))
		self.sprites.append(pygame.image.load('attack_4.png'))
		self.sprites.append(pygame.image.load('attack_5.png'))
		self.sprites.append(pygame.image.load('attack_6.png'))
		self.sprites.append(pygame.image.load('attack_7.png'))
		self.sprites.append(pygame.image.load('attack_8.png'))
		self.sprites.append(pygame.image.load('attack_9.png'))
		self.sprites.append(pygame.image.load('attack_10.png'))
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x,pos_y]

	def attack(self):
		self.attack_animation = True

	def update(self,speed):
		if self.attack_animation == True:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0
				self.attack_animation = False

		self.image = self.sprites[int(self.current_sprite)]

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Sprite Animation")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(100,100)
moving_sprites.add(player)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			player.attack()

	# Drawing
	screen.fill((0,0,0))
	moving_sprites.draw(screen)
	moving_sprites.update(0.25)
	pygame.display.flip()
	clock.tick(60)

# option 3:

# player:
class Player:
        live = True
        speed = 15

        left = False
        right = False
        up = False
        down = False

        width = 80
        height = 80

        sonido_f = pygame.mixer.Sound("music/muerte.mp3")

        speed_sprite = 0.1

        def __init__(self, window_size):
                self.x = window_size[0]//2 - 45
                self.y = window_size[1]//2 - 25
                
                self.rect = pygame.Rect(self.x,self.y, self.width, self.height)

                func = lambda img: pygame.image.load(img)

                self.images = [func(i) for i in ['images/player/player10.png', 'images/player/player11.png']]
                self.images_up = [func(i) for i in ['images/player/player0.png', 'images/player/player1.png', 'images/player/player2.png']]
                self.images_down = [func(i) for i in ['images/player/player3.png', 'images/player/player4.png', 'images/player/player5.png']]
                self.images_left = [func(i) for i in ['images/player/player8.png', 'images/player/player9.png']]
                self.images_right = [func(i) for i in ['images/player/player6.png', 'images/player/player7.png']]
                        
                self.actual = 0
                self.image = self.images[self.actual]
        
        def down_key(self,key):
                if key == K_a:
                        self.left = True
                if key == K_d:
                        self.right = True
                if key == K_w:
                        self.up = True
                if key == K_s:
                        self.down = True
                        
        def up_key(self,key):
                if key == K_a:
                        self.left = False
                if key == K_d:
                        self.right = False
                if key == K_w:
                        self.up = False
                if key == K_s:
                        self.down = False
                        
        def moving_player(self, screen):
                now = self.images
                
                if self.left:
                        self.rect.x -= self.speed
                        now = self.images_left
                if self.right:
                        self.rect.x += self.speed
                        now = self.images_right
                if self.up:
                        self.rect.y -= self.speed
                        now = self.images_up
                if self.down:
                        self.rect.y += self.speed
                        now = self.images_down
                
                screen.blit(self.image, self.get_position())
                self.changues_img(now)

        def changues_img(self, sprites):
                if self.actual >= len(sprites):
                        self.actual = 0
                self.image = sprites[int(self.actual)]
                self.actual += self.speed_sprite
                
        def get_position(self):
                return (self.rect.x, self.rect.y)
        
        def set_position(self,x,y):
                self.rect.topleft = [x, y]
                
        def get_collider(self):
                return self.rect

        def set_player_live(self, live):
                self.live = live
                self.sonido_f.play()
                
        def player_live(self):
                return self.live

# (13) ------------------------------------ pog game  ---------------------------------- #

import pygame, sys, random
from pygame.locals import *

clock = pygame.time.Clock()
pygame.init()

screen_width,screen_height = 1200,600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('pong')


ball = pygame.Rect(screen_width/2 - 15,screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width-20,screen_height/2 - 70,10,140)
opponent = pygame.Rect(10,screen_height/2 - 70,10,140)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)


ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))

def ball_animation():
        global ball_speed_x, ball_speed_y
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        if ball.top <= 0 or ball.bottom >= screen_height:
                ball_speed_y *= -1
        if ball.left <= 0 or ball.right >= screen_width:
                ball_restart()

        if ball.colliderect(player) or ball.colliderect(opponent):
                ball_speed_x *= -1

def player_animation():
        player.y += player_speed
        if player.top <= 0:
                player.top = 0
        if player.bottom >= screen_height:
                player.bottom = screen_height

def opponent_animation():
        if opponent.top < ball.y:
                opponent.top += opponent_speed
        if opponent.bottom > ball.y:
                opponent.bottom -= opponent_speed
        if opponent.top <= 0:
                opponent.top = 0
        if opponent.bottom >= screen_height:
                opponent.bottom = screen_height

def ball_restart():
        global ball_speed_x, ball_speed_y
        ball.center = (screen_width/2, screen_height/2)
        ball.x *= random.choice((1,-1))
        ball.y *= random.choice((1,-1))
        
player_speed = 0
opponent_speed = 7

while True:
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit() 
                        sys.exit()
                if event.type == KEYDOWN:
                        if event.key == K_DOWN:
                                player_speed += 7
                        if event.key == K_UP:
                                player_speed -= 7
                if event.type == KEYUP:
                        if event.key == K_DOWN:
                                player_speed -= 7
                        if event.key == K_UP:
                                player_speed += 7

        ball_animation()
        player_animation()
        opponent_animation()
        
        screen.fill(bg_color)
        pygame.draw.rect(screen,light_grey, player)
        pygame.draw.rect(screen,light_grey,opponent)
        pygame.draw.ellipse(screen,light_grey,ball)
        pygame.draw.aaline(screen, light_grey, (screen_width/2,0),(screen_width/2,screen_height))

        
        pygame.display.update()
        clock.tick(30)

# (14) ------------------------------------ camera  ---------------------------------- #

# option 1:
import pygame, sys
from pygame.locals import *

clock = pygame.time.Clock()
pygame.init()

screen_width, screen_height = 600, 400

screen = pygame.display.set_mode((screen_width, screen_height))
display = pygame.Surface((1200, 1200))

class PlayerCamera:
        x, y = screen_width/2 -10, screen_height/2 -15  # the player always is in the center of the camera(screen)
        
        speed = 15
        left = False
        right = False
        up = False
        down = False

        player_collider = pygame.Rect(x,y,40,40)
        
        def down_key(self,key):
                if key == K_LEFT:
                        self.left = True
                if key == K_RIGHT:
                        self.right = True
                if key == K_UP:
                        self.up = True
                if key == K_DOWN:
                        self.down = True
                        
        def up_key(self,key):
                if key == K_LEFT:
                        self.left = False
                if key == K_RIGHT:
                        self.right = False
                if key == K_UP:
                        self.up = False
                if key == K_DOWN:
                        self.down = False
                        
        def moving_player(self, display):
                pygame.draw.rect(display,(255,255,255),self.player_collider)
                x, y = 0, 0
                if self.left:
                        x -= self.speed
                if self.right:
                        x += self.speed
                if self.up:
                        y -= self.speed
                if self.down:
                        y += self.speed
                return x, y
                
        def get_position(self):
                return (self.x, self.y)
        
        def set_position(self,x,y):
                self.x = x
                self.y = y
                
        def get_collider(self):
                return self.player_collider


player = PlayerCamera()
x_player, y_player = 0, 0


while True:
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit() 
                        sys.exit()
                if event.type == KEYDOWN:
                        player.down_key(event.key)
                if event.type == KEYUP:
                        player.up_key(event.key)
                        
        screen.fill((0,0,0)) # camera of character
        display.fill((0,0,0))  # map
        
        pygame.draw.rect(display,(255,255,255),(599,0,2,1200))
        pygame.draw.rect(display,(255,255,255),(0,599,1200,2))
        pygame.draw.circle(display,(255,255,255),(600,600),10)
                        
        screen.blit(display, (x_player, y_player))
        x, y = player.moving_player(screen)
        x_player -= x
        y_player -= y
        
        pygame.display.update()
        clock.tick(30)

#option 2: 
	# pass

# (15) --------------------------------- Gun, Bullet, direction vectors  ---------------------------------- #

# Bullet:

class Bullet:
        r_x = 0
        r_y = 0
        x = 0
        y = 0
        h = 0
        k = 0
        
        theta = 0
        x_cos = 0
        y_sin = 0
        
        magnitude = 0
        speed = 10
        limit = 200
        
        can = False
        
        def shoot(self, display):
                if self.can:
                        x = (self.magnitude * self.x_cos) + self.h
                        y = (self.magnitude * self.y_sin) + self.k

                        pygame.draw.circle(display,(255,255,255),(x,y),10)

                        if self.magnitude > self.limit:
                                self.can = False
                                self.magnitude = 0
                        else:
                                self.magnitude += self.speed
                        
        def distance(self):
                # (x - h, y - k)
                self.r_x = self.x - self.h
                self.r_y = self.y - self.k
                # self.limit =  int(math.sqrt((self.x)**2 + (self.y)**2))
        
        def angle(self):
                # 0 - 90   : +
                # 90 - 180 : -
                # 180 - 270: +
                # 270 - 360: -
                if int(self.r_x)==0:
                        self.r_x = 0.0001
                self.theta =  math.degrees(math.atan(self.r_y / self.r_x))
                if self.theta < 0 :
                        if self.r_y < 0:
                                self.theta += 360
                        else:
                                self.theta += 180
                else:
                        if self.r_x < 0:
                                self.theta += 180
                                
                self.x_cos = math.cos(math.radians(self.theta))
                self.y_sin = math.sin(math.radians(self.theta))
        
        def limit_shoot(self, position, player): # (mouse position, player position)
                self.h, self.k = player
                self.x, self.y = position
                self.can = True
                self.distance()
                self.angle()


# Gun:

class Bullet:
        r_x = 0
        r_y = 0
        x = 0
        y = 0
        h = 0
        k = 0
        
        theta = 0
        x_cos = 0
        y_sin = 0
        
        magnitude = 0
        speed = 10
        limit = 200
        
        def shoot(self, display):

                x = (self.magnitude * self.x_cos) + self.h
                y = (self.magnitude * self.y_sin) + self.k

                pygame.draw.circle(display,(255,255,255),(x,y),10)

                if self.magnitude > self.limit:
                        return False
                else:
                        self.magnitude += self.speed
                        return True
                
        def distance(self):
                # (x - h, y - k)
                self.r_x = self.x - self.h
                self.r_y = self.y - self.k
        
        def angle(self):
                # 0 - 90   : +
                # 90 - 180 : -
                # 180 - 270: +
                # 270 - 360: -
                if int(self.r_x)==0:
                        self.r_x = 0.0001
                self.theta =  math.degrees(math.atan(self.r_y / self.r_x))
                if self.theta < 0 :
                        if self.r_y < 0:
                                self.theta += 360
                        else:
                                self.theta += 180
                else:
                        if self.r_x < 0:
                                self.theta += 180
                                
                self.x_cos = math.cos(math.radians(self.theta))
                self.y_sin = math.sin(math.radians(self.theta))
        
        def limit_shoot(self, position, player):
                self.h, self.k = player
                self.x, self.y = position
                self.distance()
                self.angle()


class Gun:
        bullets = []
        bullets_activate = []

        def update_gun(self, display):
                if self.bullets:
                        for i in range(len(self.bullets)):
                                if self.bullets[i].shoot(display):
                                        self.bullets_activate.append(self.bullets[i])
                                        
                        self.bullets = self.bullets_activate.copy()
                        self.bullets_activate = []

        def activate_gun(self, position, player):
                blt = Bullet()
                blt.limit_shoot(position, player)
                
                self.bullets.append(blt)
   
pistol = Gun()

while True:
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit() 
                        sys.exit()
                if event.type == KEYDOWN:
                        player.down_key(event.key)
                        if event.key == K_SPACE:
                                pistol.activate_gun(pygame.mouse.get_pos(), player.get_position())  # get position mouse and player position.
                if event.type == KEYUP:
                        player.up_key(event.key)
                        
        display.fill((0,0,0))
        
        pistol.update_gun(display)
    
        player.moving_player(display)

        pygame.draw.aaline(display, (0,255,0), player.get_position(),pygame.mouse.get_pos()) # line type directional of gun.
        
        pygame.display.update()
        clock.tick(30)



# option 2 :

import math, pygame, random

pygame.init()

class Direccion:  # Padre
        resultante_x = 0
        resultante_y = 0
        
        x = 0
        y = 0
        
        h = 0
        k = 0
        
        theta = 0
        x_cos = 0
        y_sin = 0
        
        magnitud = 0

        collider = pygame.Rect(0,0,0,0)
        
        def mover_collider(self):
                self.collider.x = (self.magnitud * self.x_cos) + self.h
                self.collider.y = (self.magnitud * self.y_sin) + self.k
                
        def vector_respecto_al_origen(self):
                # (resultante_x, resultante_y) = (x - h, y - k)
                self.resultante_x = self.x - self.h
                self.resultante_y = self.y - self.k
        
        def calcular_angulo(self):
                # [0 - 180]   : +
                # (180 - 360] : -
                
                # atan2: [-pi,pi] # atan: [-pi/2, pi/2]
                self.theta =  math.degrees(math.atan2(self.resultante_y, self.resultante_x))
                
                if self.theta < 0:
                        self.theta += 360.0
                                
                self.x_cos = math.cos(math.radians(self.theta))
                self.y_sin = math.sin(math.radians(self.theta))

        def get_collider(self):
                return self.collider
        
        def get_position(self):
                return (self.collider.x, self.collider.y)
        

class Bullet(Direccion):  # Hijo(Padre) : hereda los atributos y metodos del padre.
        speed = 20
        limit = 700

        radius = 10
        
        def __init__(self):
                self.collider= pygame.Rect(0,0,self.radius,self.radius)
        
        def shoot(self, screen):
                self.mover_collider()

                pygame.draw.circle(screen, (255,255,255), self.get_position(), self.radius)

                if self.magnitud > self.limit:
                        return False
                else:
                        self.magnitud += self.speed
                        return True
                
        def init_shoot(self, vector_position, player_position):
                self.h, self.k = player_position
                self.x, self.y = vector_position
                
                self.vector_respecto_al_origen()
                self.calcular_angulo()


class Gun:
        bullets = []
        bullets_activate = []

        store = 10
        limit_store = 30
        ammunition = 10

        def update_gun(self, screen):
                if self.bullets:
                        for bullet in self.bullets:
                                if bullet.shoot(screen):
                                        self.bullets_activate.append(bullet)
                                        
                        self.bullets = self.bullets_activate.copy() # usamos ".copy()" para evitar la mismidad
                        self.bullets_activate = []

        def activate_gun(self, vector_position, player_position):
                if self.store > 0:
                        bullet = Bullet()
                        bullet.init_shoot(vector_position, player_position)
                        
                        self.bullets.append(bullet)

                        self.store -= 1

##        def reload_ammunition(self):
##                for i in range(self.ammunition):
##                        if self.limit_store > self.store:
##                                self.store += 1
##                        else:
##                                break
                        
        def reload_ammunition(self):  # recursividad
                if self.ammunition == 0:
                        self.ammunition = 10
                else:
                        if self.store < self.limit_store:
                                self.store += 1
                                self.ammunition -= 1
                                self.reload_ammunition()

                        
        def get_ammunition(self):
                return self.store

        def get_colliders(self):
                return self.bullets
        
        
class Enemy(Direccion):
        range_speed = [2, 5, 10, 20]
        width = 100
        height = 80
        
        def __init__(self, size_screen):
                begin = -10
                
                if random.randint(0,1):
                        self.h = random.choice([begin, size_screen[0]])
                        self.k = random.randint(begin, size_screen[1])
                else:
                        self.h = random.randint(begin, size_screen[0])
                        self.k = random.choice([begin, size_screen[1]])

                self.collider = pygame.Rect(self.h, self.k, self.width, self.height)
                
                img = random.choice(['images/otaku_1.png', 'images/otaku_2.png','images/viejo.png','images/rosel.png'])
                self.enemy_image = pygame.transform.scale(pygame.image.load(img), (self.width, self.height))
                
                self.magnitud = random.choice(self.range_speed)
        
        def follow_player(self, screen, player_position):
                self.x, self.y = player_position
                self.h, self.k = self.get_position()
                
                self.vector_respecto_al_origen()
                self.calcular_angulo()

                self.mover_collider()

                screen.blit(self.enemy_image, self.get_position())


class Orda:
        enemys = []
        enemys_activate = []
        
        t = 0
        limit_t = 50

        score = 0
        font = pygame.font.Font(None,50)
        
        def __init__(self, size_screen):
                self.size_screen = size_screen

        def update_enemys(self, screen, player, pistol):
                for enemy in self.enemys:
                        enemy.follow_player(screen, player.get_position())

                        state = True
                        for bullet in pistol.get_colliders():
                                if enemy.get_collider().colliderect(bullet.get_collider()):
                                        state = False
                                        #enemy.magnitud = -5  # if comment state = False and activate this line, when the enemys colliderect with the bullet it back off.
                        if state:
                               self.enemys_activate.append(enemy)
                        else:
                                self.score += 1
                               
                        if enemy.get_collider().colliderect(player.get_collider()):
                                print('end game')
                                player.set_player_live(False)
                                
                self.enemys = self.enemys_activate.copy()  # usamos ".copy()" para evitar la mismidad
                self.enemys_activate = []

                if self.t < self.limit_t:
                        self.t += 1
                else:
                        self.activate_enemy()
                        self.t = 0

                self.show_score(screen)

        def activate_enemy(self):
                enemy = Enemy(self.size_screen)
                self.enemys.append(enemy)

        def show_score(self, screen):
                message = self.font.render('score: '+ str(self.score), 1, (255,255, 255))
                screen.blit(message, (self.size_screen[0]-170,10))

    
# (16) ------------------------------------ particulas : particles  ---------------------------------- #

import pygame, sys, random
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 500),0,32)

def circle_surf(radius, color):
    surf = pygame.Surface((radius * 2, radius * 2))
    pygame.draw.circle(surf, color, (radius, radius), radius)
    surf.set_colorkey((0, 0, 0))
    return surf

# [localitation x & y, velocity, timer]
particles = []

while True:
    screen.fill((0,0,0))

    pygame.draw.rect(screen, (50, 20, 120), pygame.Rect(100, 100, 200, 80))

    mx, my = pygame.mouse.get_pos()
    particles.append([[mx, my], [random.randint(0,20) / 10 -1, -5], random.randint(6, 20)]) # random.uniform(-1,1) <==> random.randint(0,20) / 10 -1

    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1
        particle[1][1] += 0.15
        
        pygame.draw.circle(screen, (255, 255, 255), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))

        radius = particle[2] * 2
        screen.blit(circle_surf(radius, (255, 0, 0)), (int(particle[0][0] - radius), int(particle[0][1] - radius)), special_flags=BLEND_RGB_ADD)

        if particle[2] <= 0:
            particles.remove(particle)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    mainClock.tick(60)


# (17) ------------------------------------ input text  ---------------------------------- #
# (18) ------------------------------------ input text  ---------------------------------- #
# (19) ------------------------------------ input text  ---------------------------------- #
# (20) ------------------------------------ input text  ---------------------------------- #
# (21) ------------------------------------ input text  ---------------------------------- #
# (22) ------------------------------------ input text  ---------------------------------- #
# (23) ------------------------------------ input text  ---------------------------------- #
