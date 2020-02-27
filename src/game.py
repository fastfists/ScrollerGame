import pygame
import pyscroll
from . import entities
from .map import load_map, create_walls, add_mobs


def render_status(player, size) -> pygame.Surface:
    width, height = size

    # Health ###
    health_prop = player.health / player.max_health
    health_foreground = pygame.Surface((health_prop * width, height))
    health_foreground.fill((0, 255, 0))

    health_bar = pygame.Surface((width, height))
    health_bar.blit(health_foreground, (0, 0))

    # Energy ###
    energy_prop = player.energy / player.max_energy
    energy_foreground = pygame.Surface((energy_prop * (width/2), height))
    energy_foreground.fill((0, 0, 255))

    energy_bar = pygame.Surface((width, height))
    energy_bar.blit(energy_foreground, (0, 0))

    # Status ###
    status = pygame.Surface((width, height*2))
    status.blit(health_bar, (0, 0))
    status.blit(energy_bar, (0, height))
    status.set_colorkey((0, 0, 0))

    return status


class Game:

    def setup(self):
        pygame.init()
        self.screen_size = (960, 600)

        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Scroller Game")

        self.clock = pygame.time.Clock()

        self.map_data = load_map("map4")
        self.map = pyscroll.TiledMapData(self.map_data)
        self.map_layer = pyscroll.BufferedRenderer(self.map, self.screen_size)
        self.map_layer.zoom = 3

        self.walls = create_walls(self.map_data)
        self.player = entities.Player.basic_player(self)
        self.enemies = pygame.sprite.Group()
        add_mobs(self, self.map_data)

        self.all_sprites = pyscroll.PyscrollGroup(map_layer=self.map_layer)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.enemies)
        self.all_sprites.center(self.player.rect.center)

    def run(self):
        self.running = True
        while self.running:

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
        status = render_status(self.player, (400, 20))
        self.screen.blit(status, (0,0))

    def events(self):
        # Handles multiple key presses at once
        key = pygame.key.get_pressed()
        player_moved = False
        running = key[pygame.K_LSHIFT] or key[pygame.K_RSHIFT]
        if key[pygame.K_w]:
            self.player.jump()
        if key[pygame.K_d]:
            player_moved = True
            if running:
                self.player.run_right()
            else:
                self.player.walk_right()
        if key[pygame.K_a]:
            player_moved = True
            if running:
                self.player.run_left()
            else:
                self.player.walk_left()
        if player_moved:
            self.player.state.set("Walking")
        else:
            self.player.state.set("Idle")

        # Looks at past events and only runs it once
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                continue
            if event.type == pygame.KEYDOWN:
                continue

    def quit(self):
        pygame.quit()
