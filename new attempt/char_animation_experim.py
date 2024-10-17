import pygame.transform
import pygame
import spritesheet_frames
import os
os.chdir('D:\\Uni\\HIT137\\Python\\City Escape\\useless files')

FPS = 60
SCREENWIDTH = 1344
SCREENHEIGHT = 756
BG = (0, 0, 0)

char_frame = (300, 150)

class Animation_steps():
    animation_steps_WR = 6
    animation_steps_SR = 12
    animation_steps_RR = 8
    animation_steps_RLR = 12
    animation_steps_M1R = 6
    animation_steps_M2R = 3
    animation_steps_JR = 11
    animation_steps_IR = 6
    animation_steps_HR = 2
    animation_steps_DR = 4


class Animation:
    def __init__(self):
        self.animation_list ={
            "WR": [],
            "SR": [],
            "RR": [],
            "RLR": [],
            "M1R": [],
            "M2R": [],
            "JR": [],
            "IR": [],
            "HR": [],
            "DR": [],
        }
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 110
        self.frame = 0
        self.current_direction = None

        self.load_animations()
    
    def load_animations(self):

        sprite_sheet_mapping = {
            "WR": spritesheet_frames.char_WR_sprite_sheet,
            "SR": spritesheet_frames.char_SR_sprite_sheet,
            "RR": spritesheet_frames.char_RR_sprite_sheet,
            "RLR": spritesheet_frames.char_RLR_sprite_sheet,
            "M1R": spritesheet_frames.char_M1R_sprite_sheet,
            "M2R": spritesheet_frames.char_M2R_sprite_sheet,
            "JR": spritesheet_frames.char_JR_sprite_sheet,
            "IR": spritesheet_frames.char_IR_sprite_sheet,
            "HR": spritesheet_frames.char_HR_sprite_sheet,
            "DR": spritesheet_frames.char_DR_sprite_sheet,
        }

        for direction, sprite_sheet in sprite_sheet_mapping.items():
            anim_dir = f"get_image{direction}"

            if hasattr(spritesheet_frames.sprite_frame, anim_dir):
                get_image_method = getattr(spritesheet_frames.sprite_frame, anim_dir)
                
                for x in range(Animation_steps.__dict__[f"animation_steps_{direction}"]):
                    frame = get_image_method(sprite_sheet, x, 128, 128, 2.5)
                    self.animation_list[direction].append(frame)

                    if "R" in direction:
                        flipped_frame = pygame.transform.flip(frame, True, False)
                        self.animation_list.setdefault(direction.replace("R", "L"), []).append(flipped_frame)
    
    def update_animation(self, direction):
        if direction != self.current_direction:
            self.current_direction = direction
            self.frame = 0
        
        if direction in self.animation_list and self.animation_list[direction]:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update >= self.animation_cooldown:
                self.frame += 1
                self.last_update = current_time
                if self.frame >= len(self.animation_list[direction]):
                    self.frame = 0
    
    def draw(self, screen, direction, position):
        if direction in self.animation_list and self.animation_list[direction]:
            if self.frame < len(self.animation_list[direction]):
                scaled_frame = pygame.transform.scale(self.animation_list[direction][self.frame], (400, 400))
                screen.blit(scaled_frame, position)
            else:
                print(f"Frame inds out of range for direction '{direction}': {self.frame} >= {len(self.animation_list[direction])}")
        else:
            print(f"No frames available for direction: {direction}")    

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    clock = pygame.time.Clock()
    animation = Animation()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        screen.fill(BG)

        animation.update_animation("IR")
        animation.draw(screen, "IR", (char_frame))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()




