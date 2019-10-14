import pygame
from pygame import sprite
from . import entities

class Game:
    # initialize pygame

    def setup(self):
        pygame.init()
        self.screen_size = (700, 500)

        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Scroller Game")

        self.clock = pygame.time.Clock()

        player = entities.get_player()
        all_sprites = pygame.sprite.SpriteGroup()
        all_sprites.add(player)

    def run(self):
        self.running = True
        while self.running:
            self.events()
            self.screen.fill((0,0,0))
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)

        self.quit()

    def update(self):
        all_sprites.update()

    def draw(self):
        all_sprites.draw(self.screen)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def quit(self):
        pygame.quit()

