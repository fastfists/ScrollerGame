from .entity import Entity
import pygame


class Player(Entity):

    max_energy = 100

    energy = 75
    energy_reload = 0.25

    max_health = 100
    health = 100

    gravity = 1

    y_vel = 0
    speed = 7

    def move_left(self, speed=None):
        self.energy -= 1
        if speed is None:
            speed = self.speed
        self.rect.x -= speed

    def move_right(self, speed=None):
        self.energy -= 1
        if speed is None:
            speed = self.speed
        self.rect.x += speed

    def update(self, game):
        print(self.state.get())
        if self.state.get() == "Jumping":
            self.y_vel += self.gravity
            self.rect.y += self.y_vel

            if self.rect.bottom == game.screen_size[1]:
                self.state.set("Idle", override=True)

        if self.energy < self.max_energy:
            self.energy += self.energy_reload

    def jump(self):
        if self.state.get() == "Jumping":
            return

        self.energy -= 3
        self.y_vel = -self.speed*3
        self.state.set("Jumping", override=True)
        self.jump_start = self.rect.bottom
