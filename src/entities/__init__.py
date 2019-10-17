import pygame
from .state import State
from .entity import Entity
from .player import Player

def get_player(game):
    
    state = State(noraml_states={"Idle"})

    size = 16, 32
    surface = pygame.Surface(size)
    surface.fill((255, 0, 0))

    rect = surface.get_rect()
    rect.bottomleft = (0, game.screen_size[1])
    rect.size = size

    image_ref = { "Idle" : [surface], "Jumping": [surface] } 

    return Player(state=state, image_ref=image_ref, rect= rect)
