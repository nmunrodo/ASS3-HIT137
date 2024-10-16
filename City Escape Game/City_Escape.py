import pygame.display
import pygame.surface
import pygame.transform
import pygame
import pygame.sprite
import os
import Plax_BG
from pygame.locals import *
#import char_animation_experim

pygame.init()
pygame.display.init()
pygame.display.set_mode((1344, 756))
clock = pygame.time.Clock()
os.chdir('D:\\Uni\\HIT137\\Python\\City Escape')

# Game window
FPS = 60
SCREENWIDTH = 1344
SCREENHEIGHT = 756
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("City Escape")

#GAM VAR
char_frame = (300, 150)
sx = 500
sy = 500
width = 128
height = 128
vel = 2
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0
isJump = False
jumpCount = 10

#game loop
run = True
while run:

    clock.tick(FPS)
    Plax_BG.draw_bg()
    Plax_BG.draw_ground()
    
    
    pygame.display.update()    
   #controls
    keys = pygame.key.get_pressed()
       
    if keys[pygame.K_LEFT] and Plax_BG.scroll > 0:
        Plax_BG.scroll -= vel
        left = True
        right = False


    if keys[pygame.K_RIGHT] and Plax_BG.scroll < 10000 - width - vel:
     
        Plax_BG.scroll += vel
        right = True
        left = False

          
    else:
        right = False
        left = False
        walkCount = 0


    if not (isJump):   
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
        if jumpCount < 0:
            neg = -1
            sy -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

    #illustrate Background



pygame.quit()