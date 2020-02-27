from .entity import Entity
from .state import State
import pygame


class Enemy(Entity):

    direction = 1
    speed = 1
    max_pace = 3

    @classmethod
    def basic_enemy(cls, x, y, **kw):
        state = State(
                default_state="Walking",
                noraml_states={"Walking"},
                unstopable_states={"Jumping"})

        size = 16, 16*2
        surface = pygame.Surface(size)
        surface.fill((0, 0, 255))

        rect = surface.get_rect()
        rect.x, rect.y = x, y
        image_ref = {"Walking": [surface]}
        return cls(state=state, image_ref=image_ref, rect=rect, **kw)

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

    @classmethod
    def basic_enemy(cls, x, y, **kw):

        state = State(
                default_state="Walking",
                noraml_states={"Walking"},
                unstopable_states={"Jumping"})

        size = 8*2, 8
        surface = pygame.Surface(size)
        surface.fill((0, 255, 0))

        rect = surface.get_rect()
        rect.x, rect.y = x, y
        image_ref = {"Walking": [surface]}
        return cls(state=state, image_ref=image_ref, rect=rect, **kw)

    def __init__(self, **kw):
        super().__init__(**kw)
        self.start_x = self.rect.x

    def update(self, game):
        # Pace
        self.rect.x += self.speed*self.direction

        if abs(self.rect.x - self.start_x) >= self.rect.width*self.max_pace:
            self.direction = -self.direction
