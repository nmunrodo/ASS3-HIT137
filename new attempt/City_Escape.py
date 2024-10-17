from pygame import K_SPACE
import pygame.key
import pygame
import os
import Plax_BG
import char_animation_experim

pygame.init()
FPS = 60
SCREENWIDTH = 1344
SCREENHEIGHT = 756
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("City Escape")
clock = pygame.time.Clock()
os.chdir('D:\\Uni\\HIT137\\Python\\City Escape\\useless files')

# Game window
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#GAM VAR
char_frame = (300, 150)
sx = 500 
sy = 500
width = 128
height = 128
vel = 5
isJump = False
jumpCount = 10
base_y = 200
sy = 0
left = False
right = False
walkCount = 0

#game loop
gravity = 0.5

level = 1
bg = Plax_BG.ParallaxBackground(level)
animation = char_animation_experim.Animation()
char_x = 300

current_direction = "IR"
last_direction = "IR"

class Button:
    
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        font_path = 'D:\\Uni\\HIT137\\Python\\City Escape\\useless files\\confession.ttf'
        font_size = 48
        font = pygame.font.Font(font_path, font_size)
        pygame.draw.rect(screen, WHITE, self.rect)
        text_surface = font.render(self.text, True, BLACK)
        screen.blit(text_surface, (self.rect.x + (self.rect.width - text_surface.get_width()) // 2, self.rect.y + (self.rect.height - text_surface.get_height()) // 2))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

def title_screen():
    play_button = Button("PLAY", SCREENWIDTH // 2 - 100, SCREENHEIGHT // 2 - 50, 200, 100)
    exit_button = Button("QUIT", SCREENWIDTH // 2 - 100, SCREENHEIGHT // 2 + 70, 200, 100)

    while True:
        screen.fill(BLACK)
        play_button.draw(screen)
        exit_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.is_clicked(event.pos):
                    return
                if exit_button.is_clicked(event.pos):
                    pygame.quite()
                    return
        
        pygame.display.flip()
        clock.tick(FPS)

class Bullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = 10

        self.spritesheet = pygame.image.load('D:\\Uni\\HIT137\\Python\\City Escape\\useless files\\fire-trails\\bullet.jpg').convert_alpha()

        bullet_rect = pygame.Rect(1255, 365, 2488, 646)
        self.image = self.spritesheet.subsurface(bullet_rect)

    def update(self):
        if self.direction == "right":
            self.x += self.speed
        else:
            self.x -= self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
SHOOT_RIGHT_ANIM = "SR"
SHOOT_LEFT_ANIM = "SL"

isShooting = False

def main_game_loop():
    global isJump, level, char_x, bg, sy, jumpCount, isShooting, shoot_start_time
    import pygame
    jumpCount = 10
    sy = 0
    bg = Plax_BG.ParallaxBackground(level)
    char_x = 300
    isJump = False
    isShooting = False
    run = True
    level = 1
    animation = char_animation_experim.Animation()
    bullets = []
    shoot_duration = 500
    shoot_start_time = 0
    
    left = False
    right = False
    last_direction = "IR"

    while run:
        clock.tick(FPS)
        screen.fill((0, 0, 0))
        def display_level(screen, level):
            level_text = f"Level {level}"
            font_path = 'D:\\Uni\\HIT137\\Python\\City Escape\\useless files\\confession.ttf'
            font_size = 48
            font = pygame.font.Font(font_path, font_size)
            text_surface = font.render(level_text, True, (255, 255, 255))
            screen.blit(text_surface, (10, 10))

        display_level(screen, level)
    #controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
            
        if keys[pygame.K_SPACE] and not isJump and not isShooting:
            isShooting = True
            shoot_start_time = pygame.time.get_ticks()
            last_direction = "SR" if right else "SL"
            animation.update_animation(last_direction)
            bullet = Bullet(char_x + (width // 2), base_y + sy + height // 2, last_direction)  # Adjust position as needed
            bullets.append(bullet)

        if isShooting:
            if pygame.time.get_ticks() - shoot_start_time > shoot_duration:
                animation.update_animation(last_direction)
            else: 
                isShooting - False
            
               
        if not isJump:
            if keys[pygame.K_LEFT] and bg.scroll > 0:
                bg.update_scroll(-vel)
                last_direction = "WL"
                left = True
                right = False
                animation.update_animation(last_direction)

            elif keys[pygame.K_RIGHT] and bg.scroll < 2000 - width - vel:
                bg.update_scroll(vel)
                last_direction = "WR"
                right = True
                left = False
                animation.update_animation(last_direction) 
                                                        #Check this code       
            else:
                last_direction = "IR" 
                animation.update_animation(last_direction)

            if keys[pygame.K_UP]:
                isJump = True
                last_direction = "JR" if last_direction == "WR" else "JL"

        else:
            neg = 1 if jumpCount >= 0 else -1        
            sy -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1

            if jumpCount < -10:
                isJump = False
                jumpCount = 10
                sy = 0   

        for bullet in bullets[:]:
            bullet.update()
            bullet.draw(screen)   
            if bullet.x < 0 or bullet.x > SCREENWIDTH:
                bullets.remove(bullet)

       
        if bg.scroll >= 2000 - 800:
            level += 1
            if level > 3:
                level = 1
            bg = Plax_BG.ParallaxBackground(level)
            char_x = 300
            bg.scroll = 0
        
        bg.draw_bg(screen)
        bg.draw_ground(screen)
        animation.draw(screen, last_direction, (350, base_y + sy))
        display_level(screen, level)

        pygame.display.flip()

    pass

if __name__ == "__main__":
    title_screen()
    main_game_loop()



pygame.quit(), 