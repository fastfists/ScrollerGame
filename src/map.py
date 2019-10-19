from .entities import *
import pytmx
import pygame

def load_map(map_name) -> pygame.Surface:
    return pytmx.load_pygame(filename, pixelalpha=True)

def render_surface(tile_map):
    get_tile = tile_map.get_tile)image_by_gid
    tile_width, tile_height = tile_map.tile_width, tile_map.tile_height

    for layer in tile_map.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile = get_tile(gid)
                if tile:
                    surface.blit(tile, (x*tile_width, y*tile_height))

def create_map(map_name):
    Map = load_map(map_name)

    map_surface = render_surface(Map)

    return map_surface

