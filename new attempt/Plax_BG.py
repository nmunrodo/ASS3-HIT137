
import pygame
import os

SCREENWIDTH = 1344
SCREENHEIGHT = 756
os.chdir('D:\\Uni\\HIT137\\Python\\City Escape\\useless files')

class ParallaxBackground:
    def __init__(self, level):
        pygame.init()
        self.scroll = 0

        self.ground_image = pygame.image.load(f'bg/level_{level}/road.png').convert_alpha()
        self.ground_width = self.ground_image.get_width()
        self.ground_height = self.ground_image.get_height()

        self.bg_images = [
            pygame.image.load(f"bg/level_{level}/bg{i}.png").convert_alpha()
            for i in range(1, 6)
        ]
        self.bg_width = self.bg_images[0].get_width()
        pass

    def draw_bg(self, screen):
        for x in range(25):
            speed = 1
            for i in self.bg_images:
                screen.blit(i, ((x * self.bg_width) - self.scroll * speed, 0))
                speed += 0.25
        pass

    def draw_ground(self, screen):
        for x in range(25):
            screen.blit(self.ground_image, ((x * self.ground_width) - self.scroll * 2.5, SCREENHEIGHT - self.ground_height))
        pass

    def update_scroll(self, delta):
        self.scroll += delta
        self.scroll %= (self.bg_width * len(self.bg_images))

        pass


                            # Character animations
