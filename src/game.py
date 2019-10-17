import pygame
from . import entities

class Game:
    # initialize pygame

    current_game = None
    def setup(self):
        pygame.init()
        self.screen_size = (700, 500)

        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Scroller Game")

        self.clock = pygame.time.Clock()

        self.player = entities.get_player(self)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        Game.current_game = self

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
        self.all_sprites.update(self)

    def draw(self):
        self.screen.fill((0,0,0))
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

