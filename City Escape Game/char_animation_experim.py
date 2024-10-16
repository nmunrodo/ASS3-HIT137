
import pygame.display
import pygame
import spritesheet_frames


FPS = 60
SCREENWIDTH = 1344
SCREENHEIGHT = 756
BG = (0, 0, 0)
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
char_frame = (300, 150)


animation_list_WR = []
animation_list_WL = []
animation_list_SR = []
animation_list_SL = []
animation_list_RR = []
animation_list_RL = []
animation_list_RLR = []
animation_list_RLL = []
animation_list_M1R = []
animation_list_M1L = []
animation_list_M2R = []
animation_list_M2L = []
animation_list_JR = []
animation_list_JL = []
animation_list_IR = []
animation_list_IL = []
animation_list_HR = []
animation_list_HL = []
animation_list_DR = []
animation_list_DL = []

last_update = pygame.time.get_ticks()
animation_cooldown = 110
frame = 0
class Animation_steps():
    animation_steps_WR = 8
    animation_steps_WL = 8
    animation_steps_SR = 12
    animation_steps_SL = 12
    animation_steps_RR = 8
    animation_steps_RL = 8
    animation_steps_RLR = 12
    animation_steps_RLL = 12
    animation_steps_M1R = 6
    animation_steps_M1L = 6
    animation_steps_M2R = 3
    animation_steps_M2L = 3
    animation_steps_JR = 11
    animation_steps_JL = 11
    animation_steps_IR = 6
    animation_steps_IL = 6
    animation_steps_HR = 2
    animation_steps_HL = 2
    animation_steps_DR = 4
    animation_steps_DL = 4




    #char_anim = spritesheet_frames.sprite_frame({spritesheet_frames})
for x in range(Animation_steps.animation_steps_WR):
    animation_list_WR.append(spritesheet_frames.sprite_frame.get_imageWR(spritesheet_frames.char_WR_sprite_sheet, x, 128, 128, 2.5))
'''    
pygame.init()
run = True
while run:
'''
    #update BG
    #screen.fill(BG)
for x in range(Animation_steps.animation_steps_WR):

#update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list_WR):
            frame = 0
    def WR_anim():
        screen.blit(animation_list_WR[frame], (char_frame))
'''        
        pygame.display.update()
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False
'''



