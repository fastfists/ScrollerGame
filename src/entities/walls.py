import pygame

class Wall(pygame.sprite.Sprite):

    def __init__(self, rect):
        super().__init__(self)
        self.rect = rect
        self.image = pygame.Surface(self.rect.size)
        self.image.fill((0, 255, 0))

