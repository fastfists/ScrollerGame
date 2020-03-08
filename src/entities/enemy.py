from .entity import Entity
from .state import State
import pygame


class Enemy(Entity):

    direction = 1
    speed = 1
    max_pace = 3


    def __init__(self, **kw):
        super().__init__(**kw)
        self.start_x = self.rect.x

    def update(self, game):
        # Pace
        self.rect.x += self.speed*self.direction

        if abs(self.rect.x - self.start_x) >= self.rect.width*self.max_pace:
            self.direction = -self.direction


class Bird(Entity):

    direction = 1
    speed = 1
    max_pace = 3

    def __init__(self, **kw):
        super().__init__(**kw)
        self.start_x = self.rect.x

    def update(self, game):
        # Pace
        self.rect.x += self.speed*self.direction

        if abs(self.rect.x - self.start_x) >= self.rect.width*self.max_pace:
            self.direction = -self.direction
