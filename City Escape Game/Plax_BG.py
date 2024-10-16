import pygame.display
import pygame.surface
import pygame.transform
import pygame
import pygame.sprite
import os
from pygame.locals import *
os.chdir('D:\\Uni\\HIT137\\Python\\City Escape')

pygame.init()

clock = pygame.time.Clock()

FPS = 60

SCREENWIDTH = 1344
SCREENHEIGHT = 756
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("City Escape")


#Paralax backgroung 
scroll = 0
ground_image = pygame.image.load('bg/level_1/road.png').convert_alpha()
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()


bg_images_L1 = []
for i in range(1, 6):
    bg_image = pygame.image.load(f"bg/level_1/bg{i}.png").convert_alpha()
    bg_images_L1.append(bg_image)
bg_width = bg_images_L1[0].get_width()

def draw_bg():
    for x in range(25):
        vel = 3
        for i in bg_images_L1:
            screen.blit(i, ((x * bg_width) - scroll * vel, 0))
            vel += 0.25

def draw_ground():
    for x in range(25):
       screen.blit(ground_image, ((x * ground_width) - scroll * 2.5, SCREENHEIGHT - ground_height))

pygame.display.update()