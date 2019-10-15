import pygame
from .state import State
from .entity import Entity
from .player import Player

def get_player():

    state = State(noraml_states={"Idle"})

    size = 16, 32
    surface = pygame.Surface(size)
    surface.fill((255, 0, 0))

    rect = surface.get_rect()
    rect.topleft = (0, 0)
    rect.size = (32, 16)

    image_ref = { "Idle" : [surface] } 

    return Player(state=state, image_ref=image_ref, rect= rect)
    

