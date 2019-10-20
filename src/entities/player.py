from .entity import Entity
import pygame


class Player(Entity):

    max_energy = 100

    energy = 50
    energey_reload = 0.25

    max_health = 100
    health = 100

    gravity = 1

    y_vel = 0
    speed = 7

    def move_left(self, speed=None):
        if speed is None:
            speed = self.speed
        self.rect.x -= speed

    def move_right(self, speed=None):
        if speed is None:
            speed = self.speed
        self.rect.x += speed

    def update(self, game):
        if self.state.get() == "Jumping":
            print(self.rect.bottomleft)
            self.y_vel += self.gravity
            self.rect.y += self.y_vel

            if self.rect.bottom == game.screen_size[1]:
                self.state.set("Idle")

    def jump(self):
        if self.state.get() == "Jumping":
            return

        self.y_vel = -self.speed*3
        self.state.set("Jumping")
        self.jump_start = self.rect.bottom
