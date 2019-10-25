import pygame
from .state import State
from .entity import Entity
from .player import Player
from .enemy import Enemy

def get_player(game):

    state = State(noraml_states={"Idle", "Walking"}, unstopable_states={"Jumping"})

    size = 16, 16*2
    surface = pygame.Surface(size)
    surface.fill((255, 0, 0))

    rect = surface.get_rect()
    image_ref = { "Idle" : [surface], "Jumping": [surface], "Walking" : [surface]}

    return Player(state=state, image_ref=image_ref, rect= rect)

