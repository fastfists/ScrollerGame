import pygame

class Wall(pygame.sprite.Sprite):

    def __init__(self, rect, image):
        super().__init__(self)
        self.rect = rect
        self.image = pygame.Surface(self.rect.sizeself.rect.sizeself.rect.size)
        self.image.fill((0, 255, 0))
