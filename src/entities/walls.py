import pygame

class Wall(pygame.sprite.Sprite):

    def __init__(self, rect, groups=[]):
        super().__init__(*groups)
        self.rect = rect

