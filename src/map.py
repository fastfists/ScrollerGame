from .entities import *
import pytmx
import pygame
from os import path
from src.entities.walls import Wall
from src.entities.enemy import Enemy

def load_map(map_name) -> pygame.Surface:
    filename = path.join('assets/maps/', map_name+'.tmx')
    return pytmx.load_pygame(filename, pixelalpha=True)

def render_surface(tile_map):
    get_tile = tile_map.get_tile_image_by_gid
    tile_width, tile_height = tile_map.tilewidth, tile_map.tileheight
    surface = pygame.Surface((tile_map.width*tile_width, tile_height*tile_map.height))

    for layer in tile_map.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile = get_tile(gid)
                if tile:
                    surface.blit(tile, (x*tile_width, y*tile_height))

    return surface

def create_surface(map_name):
    Map = load_map(map_name)

    map_surface = render_surface(Map)

    return map_surface

def add_mobs(game, tile_map):
    player = game.player
    for tile in tile_map.objects:
        if tile.name == "Player":
            player.rect.x = tile.x
            player.rect.y = tile.y
        if tile.name == "Enemy":
            enemy = Enemy.basic_enemy(tile.x, tile.y)
            game.enemies.add(enemy)

def create_walls(tile_map) -> pygame.sprite.Group:

    walls = pygame.sprite.Group()
    for tile in tile_map.objects:
        if tile.name == "Wall":
            rect = pygame.Rect(tile.x, tile.y, tile.width, tile.height)
            print(rect)
            walls.add(Wall(rect, groups=[walls]))

    return walls


