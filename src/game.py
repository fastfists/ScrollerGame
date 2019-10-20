import pygame
import pyscroll
from . import entities
from .map import load_map

def render_health_bar(self, size):
    width, height = size

    health_length = current_health // self.max_health
    health_length = health_length if health_length >= 0 else 0

    foreground = pygame.Surface((health_length,height))
    foreground.fill(utils.GREEN)

    health_bar = pygame.Surface((width, height))
    health_bar.blit(self.foreground, (0,0))
    position = (0, 0)
    screen.blit(health_bar, position)

class Game:

    def setup(self):
        pygame.init()
        self.screen_size = (1600, 960)

        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Scroller Game")

        self.clock = pygame.time.Clock()

        self.map = pyscroll.TiledMapData(load_map("map2"))
        self.map_layer = pyscroll.BufferedRenderer(self.map, self.screen_size)
        self.map_layer.zoom = 2

        self.player = entities.get_player(self)

        self.all_sprites = pyscroll.PyscrollGroup(map_layer=self.map_layer)
        self.all_sprites.add(self.player)
        self.all_sprites.center(self.player.rect.center)

    def run(self):
        self.running = True
        while self.running:
            self.screen.fill((0,0,0))

            self.update()
            self.draw()

            self.events()

            pygame.display.flip()
            self.clock.tick(60)

        self.quit()

    def update(self):
        self.all_sprites.center(self.player.rect.center)
        self.all_sprites.update(self)

    def draw(self):
        self.all_sprites.draw(self.screen)

    def events(self):
        # Handles multiple key presses at once
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.player.jump()
        if key[pygame.K_d]:
            self.player.move_right()
        if key[pygame.K_a]:
            self.player.move_left()

        # Looks at past events and only runs it once
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                continue
            if event.type == pygame.KEYDOWN:
                continue

    def quit(self):
        pygame.quit()

