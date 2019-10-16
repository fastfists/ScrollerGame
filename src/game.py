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

        self.player = entities.get_player()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

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
        self.all_sprites.update()

    def draw(self):
        self.screen.fill((0,0,0))
        self.all_sprites.draw(self.screen)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                continue
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.player.jump()
                if event.key == pygame.K_d:
                    self.player.move_right()
                if event.key == pygame.K_a:
                    self.player.move_left()

                continue

    def quit(self):
        pygame.quit()

