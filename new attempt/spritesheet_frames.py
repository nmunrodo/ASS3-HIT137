from matplotlib import animation
import pygame.display
import pygame.surface
import pygame.transform
import pygame
import pygame.sprite
import os
os.chdir('D:\\Uni\\HIT137\\Python\\City Escape\\useless files')
from pygame.locals import *

pygame.display.init()
SCREENWIDTH = 1344
SCREENHEIGHT = 756
pygame.init()
clock = pygame.time.Clock()
FPS = 60
screen = pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT])


char_WR_sprite_sheet = pygame.image.load('ch_1/char_walkR.png').convert_alpha()
char_WL_sprite_sheet = pygame.image.load('ch_1/char_walkL.png').convert_alpha()
char_SR_sprite_sheet = pygame.image.load('ch_1/char_shootR.png').convert_alpha()
char_SL_sprite_sheet = pygame.image.load('ch_1/char_shootL.png').convert_alpha()
char_RR_sprite_sheet = pygame.image.load('ch_1/char_runR.png').convert_alpha()
char_RL_sprite_sheet = pygame.image.load('ch_1/char_runL.png').convert_alpha()
char_RLR_sprite_sheet = pygame.image.load('ch_1/char_reloadR.png').convert_alpha()
char_RLL_sprite_sheet = pygame.image.load('ch_1/char_reloadL.png').convert_alpha()
char_M1R_sprite_sheet = pygame.image.load('ch_1/char_m1R.png').convert_alpha()
char_M1L_sprite_sheet = pygame.image.load('ch_1/char_m1L.png').convert_alpha()
char_M2R_sprite_sheet = pygame.image.load('ch_1/char_m2R.png').convert_alpha()
char_M2L_sprite_sheet = pygame.image.load('ch_1/char_m2L.png').convert_alpha()
char_JR_sprite_sheet = pygame.image.load('ch_1/char_jumpR.png').convert_alpha()
char_JL_sprite_sheet = pygame.image.load('ch_1/char_jumpL.png').convert_alpha()
char_IR_sprite_sheet = pygame.image.load('ch_1/char_idlR.png').convert_alpha()
char_IL_sprite_sheet = pygame.image.load('ch_1/char_idlL.png').convert_alpha()
char_HR_sprite_sheet = pygame.image.load('ch_1/char_hurtR.png').convert_alpha()
char_HL_sprite_sheet = pygame.image.load('ch_1/char_hurtL.png').convert_alpha()
char_DR_sprite_sheet = pygame.image.load('ch_1/char_dieR.png').convert_alpha()
char_DL_sprite_sheet = pygame.image.load('ch_1/char_dieL.png').convert_alpha()



class sprite_frame():
    def __init__(self, image):
        self.sheet = image

    def get_imageWR(sheet, frame, width, height, scale):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        
        return image
       
    frame_WR0 = get_imageWR(char_WR_sprite_sheet, 0, 128, 128, 3.5)
    frame_WR1 = get_imageWR(char_WR_sprite_sheet, 1, 128, 128, 3.5)
    frame_WR2 = get_imageWR(char_WR_sprite_sheet, 2, 128, 128, 3.5)
    frame_WR3 = get_imageWR(char_WR_sprite_sheet, 3, 128, 128, 3.5)
    frame_WR4 = get_imageWR(char_WR_sprite_sheet, 4, 128, 128, 3.5)
    frame_WR5 = get_imageWR(char_WR_sprite_sheet, 5, 128, 128, 3.5)
            
    def get_imageWL(sheet, frame, width, height, scale):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        return image

    frame_WL0 = get_imageWL(char_WL_sprite_sheet, 0, 128, 128, 3.5)
    frame_WL1 = get_imageWL(char_WL_sprite_sheet, 1, 128, 128, 3.5)
    frame_WL2 = get_imageWL(char_WL_sprite_sheet, 2, 128, 128, 3.5)
    frame_WL3 = get_imageWL(char_WL_sprite_sheet, 3, 128, 128, 3.5)
    frame_WL4 = get_imageWL(char_WL_sprite_sheet, 4, 128, 128, 3.5)
    frame_WL5 = get_imageWL(char_WL_sprite_sheet, 5, 128, 128, 3.5)

    def get_imageSR(sheet, frame, width, height, scale):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        return image

    frame_SR0 = get_imageSR(char_SR_sprite_sheet, 0, 128, 128, 3.5)
    frame_SR1 = get_imageSR(char_SR_sprite_sheet, 1, 128, 128, 3.5)
    frame_SR2 = get_imageSR(char_SR_sprite_sheet, 2, 128, 128, 3.5)
    frame_SR3 = get_imageSR(char_SR_sprite_sheet, 3, 128, 128, 3.5)
    frame_SR4 = get_imageSR(char_SR_sprite_sheet, 4, 128, 128, 3.5)
    frame_SR5 = get_imageSR(char_SR_sprite_sheet, 5, 128, 128, 3.5)
    frame_SR6 = get_imageSR(char_SR_sprite_sheet, 6, 128, 128, 3.5)
    frame_SR7 = get_imageSR(char_SR_sprite_sheet, 7, 128, 128, 3.5)
    frame_SR8 = get_imageSR(char_SR_sprite_sheet, 8, 128, 128, 3.5)
    frame_SR9 = get_imageSR(char_SR_sprite_sheet, 9, 128, 128, 3.5)
    frame_SR10 = get_imageSR(char_SR_sprite_sheet, 10, 128, 128, 3.5)
    frame_SR11 = get_imageSR(char_SR_sprite_sheet, 11, 128, 128, 3.5)

    def get_imageSL(sheet, frame, width, height, scale):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        return image

    frame_SL0 = get_imageSL(char_SL_sprite_sheet, 0, 128, 128, 3.5)
    frame_SL1 = get_imageSL(char_SL_sprite_sheet, 1, 128, 128, 3.5)
    frame_SL2 = get_imageSL(char_SL_sprite_sheet, 2, 128, 128, 3.5)
    frame_SL3 = get_imageSL(char_SL_sprite_sheet, 3, 128, 128, 3.5)
    frame_SL4 = get_imageSL(char_SL_sprite_sheet, 4, 128, 128, 3.5)
    frame_SL5 = get_imageSL(char_SL_sprite_sheet, 5, 128, 128, 3.5)
    frame_SL6 = get_imageSL(char_SL_sprite_sheet, 6, 128, 128, 3.5)
    frame_SL7 = get_imageSL(char_SL_sprite_sheet, 7, 128, 128, 3.5)
    frame_SL8 = get_imageSL(char_SL_sprite_sheet, 8, 128, 128, 3.5)
    frame_SL9 = get_imageSL(char_SL_sprite_sheet, 9, 128, 128, 3.5)
    frame_SL10 = get_imageSL(char_SL_sprite_sheet, 10, 128, 128, 3.5)
    frame_SL11 = get_imageSL(char_SL_sprite_sheet, 11, 128, 128, 3.5)

    def get_imageRR(sheet, frame, width, height, scale):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        return image

    frame_RR0 = get_imageRR(char_RR_sprite_sheet, 0, 128, 128, 3.5)
    frame_RR1 = get_imageRR(char_RR_sprite_sheet, 1, 128, 128, 3.5)
    frame_RR2 = get_imageRR(char_RR_sprite_sheet, 2, 128, 128, 3.5)
    frame_RR3 = get_imageRR(char_RR_sprite_sheet, 3, 128, 128, 3.5)
    frame_RR4 = get_imageRR(char_RR_sprite_sheet, 4, 128, 128, 3.5)
    frame_RR5 = get_imageRR(char_RR_sprite_sheet, 5, 128, 128, 3.5)
    frame_RR6 = get_imageRR(char_RR_sprite_sheet, 6, 128, 128, 3.5)
    frame_RR7 = get_imageRR(char_RR_sprite_sheet, 7, 128, 128, 3.5)

    def get_imageRL(sheet, frame, width, height, scale):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        
        return image

    frame_RL0 = get_imageRL(char_RL_sprite_sheet, 0, 128, 128, 3.5)
    frame_RL1 = get_imageRL(char_RL_sprite_sheet, 1, 128, 128, 3.5)
    frame_RL2 = get_imageRL(char_RL_sprite_sheet, 2, 128, 128, 3.5)
    frame_RL3 = get_imageRL(char_RL_sprite_sheet, 3, 128, 128, 3.5)
    frame_RL4 = get_imageRL(char_RL_sprite_sheet, 4, 128, 128, 3.5)
    frame_RL5 = get_imageRL(char_RL_sprite_sheet, 5, 128, 128, 3.5)
    frame_RL6 = get_imageRL(char_RL_sprite_sheet, 6, 128, 128, 3.5)
    frame_RL7 = get_imageRL(char_RL_sprite_sheet, 7, 128, 128, 3.5)


    def get_imageRLR(sheet, frame, width, height, scale):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        
        return image

    frame_RLR0 = get_imageRLR(char_RLR_sprite_sheet, 0, 128, 128, 3.5)
    frame_RLR1 = get_imageRLR(char_RLR_sprite_sheet, 1, 128, 128, 3.5)
    frame_RLR2 = get_imageRLR(char_RLR_sprite_sheet, 2, 128, 128, 3.5)
    frame_RLR3 = get_imageRLR(char_RLR_sprite_sheet, 3, 128, 128, 3.5)
    frame_RLR4 = get_imageRLR(char_RLR_sprite_sheet, 4, 128, 128, 3.5)
    frame_RLR5 = get_imageRLR(char_RLR_sprite_sheet, 5, 128, 128, 3.5)
    frame_RLR6 = get_imageRLR(char_RLR_sprite_sheet, 6, 128, 128, 3.5)
    frame_RLR7 = get_imageRLR(char_RLR_sprite_sheet, 7, 128, 128, 3.5)
    frame_RLR8 = get_imageRLR(char_RLR_sprite_sheet, 8, 128, 128, 3.5)
    frame_RLR9 = get_imageRLR(char_RLR_sprite_sheet, 9, 128, 128, 3.5)
    frame_RLR10 = get_imageRLR(char_RLR_sprite_sheet, 10, 128, 128, 3.5)
    frame_RLR11 = get_imageRLR(char_RLR_sprite_sheet, 11, 128, 128, 3.5)

    def get_imageRLL(sheet, frame, width, height, scale):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        
        return image

    frame_RLL0 = get_imageRLL(char_RLL_sprite_sheet, 0, 128, 128, 3.5)
    frame_RLL1 = get_imageRLL(char_RLL_sprite_sheet, 1, 128, 128, 3.5)
    frame_RLL2 = get_imageRLL(char_RLL_sprite_sheet, 2, 128, 128, 3.5)
    frame_RLL3 = get_imageRLL(char_RLL_sprite_sheet, 3, 128, 128, 3.5)
    frame_RLL4 = get_imageRLL(char_RLL_sprite_sheet, 4, 128, 128, 3.5)
    frame_RLL5 = get_imageRLL(char_RLL_sprite_sheet, 5, 128, 128, 3.5)
    frame_RLL6 = get_imageRLL(char_RLL_sprite_sheet, 6, 128, 128, 3.5)
    frame_RLL7 = get_imageRLL(char_RLL_sprite_sheet, 7, 128, 128, 3.5)
    frame_RLL8 = get_imageRLL(char_RLL_sprite_sheet, 8, 128, 128, 3.5)
    frame_RLL9 = get_imageRLL(char_RLL_sprite_sheet, 9, 128, 128, 3.5)
    frame_RLL10 = get_imageRLL(char_RLL_sprite_sheet, 10, 128, 128, 3.5)
    frame_RLL11 = get_imageRLL(char_RLL_sprite_sheet, 11, 128, 128, 3.5)

    def get_imageM1R(sheet, frame, width, height, scale):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        
        return image

    frame_M1R0 = get_imageM1R(char_M1R_sprite_sheet, 0, 128, 128, 3.5)
    frame_M1R1 = get_imageM1R(char_M1R_sprite_sheet, 1, 128, 128, 3.5)
    frame_M1R2 = get_imageM1R(char_M1R_sprite_sheet, 2, 128, 128, 3.5)
    frame_M1R3 = get_imageM1R(char_M1R_sprite_sheet, 3, 128, 128, 3.5)
    frame_M1R4 = get_imageM1R(char_M1R_sprite_sheet, 4, 128, 128, 3.5)
    frame_M1R5 = get_imageM1R(char_M1R_sprite_sheet, 5, 128, 128, 3.5)

    def get_imageM1L(sheet, frame, width, height, scale):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        
        return image

    frame_M1L0 = get_imageM1L(char_M1L_sprite_sheet, 0, 128, 128, 3.5)
    frame_M1L1 = get_imageM1L(char_M1L_sprite_sheet, 1, 128, 128, 3.5)
    frame_M1L2 = get_imageM1L(char_M1L_sprite_sheet, 2, 128, 128, 3.5)
    frame_M1L3 = get_imageM1L(char_M1L_sprite_sheet, 3, 128, 128, 3.5)
    frame_M1L4 = get_imageM1L(char_M1L_sprite_sheet, 4, 128, 128, 3.5)
    frame_M1L5 = get_imageM1L(char_M1L_sprite_sheet, 5, 128, 128, 3.5)

    def get_imageM2R(sheet, frame, width, height, scale):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        
        return image

    frame_M2R0 = get_imageM2R(char_M2R_sprite_sheet, 0, 128, 128, 3.5)
    frame_M2R1 = get_imageM2R(char_M2R_sprite_sheet, 1, 128, 128, 3.5)
    frame_M2R2 = get_imageM2R(char_M2R_sprite_sheet, 2, 128, 128, 3.5)

    def get_imageM2L(sheet, frame, width, height, scale):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        
        return image

    frame_M2L0 = get_imageM2L(char_M2L_sprite_sheet, 0, 128, 128, 3.5)
    frame_M2L1 = get_imageM2L(char_M2L_sprite_sheet, 1, 128, 128, 3.5)
    frame_M2L2 = get_imageM2L(char_M2L_sprite_sheet, 2, 128, 128, 3.5)

    def get_imageJR(sheet, frame, width, height, scale):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        
        return image

    frame_JR0 = get_imageJR(char_JR_sprite_sheet, 0, 128, 128, 3.5)
    frame_JR1 = get_imageJR(char_JR_sprite_sheet, 1, 128, 128, 3.5)
    frame_JR2 = get_imageJR(char_JR_sprite_sheet, 2, 128, 128, 3.5)
    frame_JR3 = get_imageJR(char_JR_sprite_sheet, 3, 128, 128, 3.5)
    frame_JR4 = get_imageJR(char_JR_sprite_sheet, 4, 128, 128, 3.5)
    frame_JR5 = get_imageJR(char_JR_sprite_sheet, 5, 128, 128, 3.5)
    frame_JR6 = get_imageJR(char_JR_sprite_sheet, 6, 128, 128, 3.5)
    frame_JR7 = get_imageJR(char_JR_sprite_sheet, 7, 128, 128, 3.5)
    frame_JR8 = get_imageJR(char_JR_sprite_sheet, 8, 128, 128, 3.5)
    frame_JR9 = get_imageJR(char_JR_sprite_sheet, 9, 128, 128, 3.5)
    frame_JR10 = get_imageJR(char_JR_sprite_sheet, 10, 128, 128, 3.5)

    def get_imageJL(sheet, frame, width, height, scale):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        
        return image

    frame_JL0 = get_imageJL(char_JL_sprite_sheet, 0, 128, 128, 3.5)
    frame_JL1 = get_imageJL(char_JL_sprite_sheet, 1, 128, 128, 3.5)
    frame_JL2 = get_imageJL(char_JL_sprite_sheet, 2, 128, 128, 3.5)
    frame_JL3 = get_imageJL(char_JL_sprite_sheet, 3, 128, 128, 3.5)
    frame_JL4 = get_imageJL(char_JL_sprite_sheet, 4, 128, 128, 3.5)
    frame_JL5 = get_imageJL(char_JL_sprite_sheet, 5, 128, 128, 3.5)
    frame_JL6 = get_imageJL(char_JL_sprite_sheet, 6, 128, 128, 3.5)
    frame_JL7 = get_imageJL(char_JL_sprite_sheet, 7, 128, 128, 3.5)
    frame_JL8 = get_imageJL(char_JL_sprite_sheet, 8, 128, 128, 3.5)
    frame_JL9 = get_imageJL(char_JL_sprite_sheet, 9, 128, 128, 3.5)
    frame_JL10 = get_imageJL(char_JL_sprite_sheet, 10, 128, 128, 3.5)

    def get_imageIR(sheet, frame, width, height, scale):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        
        return image

    frame_IR0 = get_imageIR(char_IR_sprite_sheet, 0, 128, 128, 3.5)
    frame_IR1 = get_imageIR(char_IR_sprite_sheet, 1, 128, 128, 3.5)
    frame_IR2 = get_imageIR(char_IR_sprite_sheet, 2, 128, 128, 3.5)
    frame_IR3 = get_imageIR(char_IR_sprite_sheet, 3, 128, 128, 3.5)
    frame_IR4 = get_imageIR(char_IR_sprite_sheet, 4, 128, 128, 3.5)
    frame_IR5 = get_imageIR(char_IR_sprite_sheet, 5, 128, 128, 3.5)

    def get_imageIL(sheet, frame, width, height, scale):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        
        return image

    frame_IL0 = get_imageIL(char_IL_sprite_sheet, 0, 128, 128, 3.5)
    frame_IL1 = get_imageIL(char_IL_sprite_sheet, 1, 128, 128, 3.5)
    frame_IL2 = get_imageIL(char_IL_sprite_sheet, 2, 128, 128, 3.5)
    frame_IL3 = get_imageIL(char_IL_sprite_sheet, 3, 128, 128, 3.5)
    frame_IL4 = get_imageIL(char_IL_sprite_sheet, 4, 128, 128, 3.5)
    frame_IL5 = get_imageIL(char_IL_sprite_sheet, 5, 128, 128, 3.5)

    def get_imageHR(sheet, frame, width, height, scale):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        
        return image

    frame_HR0 = get_imageHR(char_HR_sprite_sheet, 0, 128, 128, 3.5)
    frame_HR1 = get_imageHR(char_HR_sprite_sheet, 1, 128, 128, 3.5)

    def get_imageHL(sheet, frame, width, height, scale):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        
        return image

    frame_HL0 = get_imageHL(char_HL_sprite_sheet, 0, 128, 128, 3.5)
    frame_HL1 = get_imageHL(char_HL_sprite_sheet, 1, 128, 128, 3.5)

    def get_imageDR(sheet, frame, width, height, scale):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        
        return image

    frame_DR0 = get_imageDR(char_DR_sprite_sheet, 0, 128, 128, 3.5)
    frame_DR1 = get_imageDR(char_DR_sprite_sheet, 1, 128, 128, 3.5)
    frame_DR2 = get_imageDR(char_DR_sprite_sheet, 2, 128, 128, 3.5)
    frame_DR3 = get_imageDR(char_DR_sprite_sheet, 3, 128, 128, 3.5)

    def get_imageDL(sheet, frame, width, height, scale):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        
        return image

    frame_DL0 = get_imageDL(char_DL_sprite_sheet, 0, 128, 128, 3.5)
    frame_DL1 = get_imageDL(char_DL_sprite_sheet, 1, 128, 128, 3.5)
    frame_DL2 = get_imageDL(char_DL_sprite_sheet, 2, 128, 128, 3.5)
    frame_DL3 = get_imageDL(char_DL_sprite_sheet, 3, 128, 128, 3.5)

# eXTRAS NOT SURE

pygame.quit()