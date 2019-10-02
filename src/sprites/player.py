import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, rect):
        super().__init__(self)

    def __init_subclass__(cls, picture:str = None,**kw):
        if picture:
            cls.image_name = picture
        super().__init_subclass__(**kw)



