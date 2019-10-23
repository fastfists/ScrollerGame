from .entity import Entity
import pygame


class Player(Entity):

    max_energy = 100
    energy = 200
    energy_reload = 0.1
    max_health = 100
    health = 100
    gravity = 1
    y_vel = 0
    speed = 7

    def move_left(self, speed=None):

        self.energy -= 1
        if self.energy <= 1:
            print(self.energy)
            self.energy += 1
            return
        if speed is None:
            speed = self.speed
        self.rect.x -= speed


    def move_right(self, speed=None):
        self.energy -= 1
        if self.energy <= 1:
            self.energy += 1
            return
        if speed is None:
            speed = self.speed
        self.rect.x += speed

    def update(self, game):
        touching_walls = pygame.sprite.spritecollideany(self, game.walls)
        if touching_walls:
            print("action")

        if self.state.get() == "Jumping":
            self.y_vel += self.gravity
            self.rect.y += self.y_vel

            if touching_walls:
                self.state.set("Idle", override=True)

        if self.energy < self.max_energy:
            self.energy += self.energy_reload

        if not touching_walls:
            self.state.set("Jumping")

    def jump(self):
        if self.state.get() == "Jumping":
            return

        self.energy -= 3
        if self.energy <= 1:
            self.energy += 3
            return

        self.y_vel = -self.speed*3
        self.state.set("Jumping", override=True)
        self.jump_start = self.rect.bottom
