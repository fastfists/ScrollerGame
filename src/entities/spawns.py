from src.entities.player import Player
from src.entities.enemy import Enemy
from src.entities.enemy import Bird
from src.spritesheet import SpriteSheet
from src.entities.state import State
import pygame


def basic_enemy(x, y, spritesheet:SpriteSheet, **kw):
    state = State(
            default_state="Walking",
            noraml_states={"Walking"})

    size = spritesheet.size

    rect = pygame.Rect((x, y), size)

    image_ref = spritesheet.process()
    return Enemy(state=state, image_ref=image_ref, rect=rect, **kw)

def basic_bird(x, y, **kw):
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
    return Bird(state=state, image_ref=image_ref, rect=rect, **kw)


def basic_player(game, spritesheet:SpriteSheet):
    state = State(
            noraml_states={"Idle", "Walking"},
            unstopable_states={"Jumping", "Dead"})

    size = spritesheet.size

    rect = pygame.Rect((0, 0), size)

    image_ref = spritesheet.process()
    return Player(state=state, image_ref=image_ref, rect=rect)