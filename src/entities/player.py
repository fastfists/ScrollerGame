from .entity import Entity
import pygame


class Player(Entity):

    max_energy = 100
    energy = 50
    energey_reload = 0.25

    max_health = 100
    health = 100

    speed = 1

    def move_left(self, speed=None):
        if speed is None:
            speed = self.speed
        self.rect.x -= speed

    def move_right(self, speed=None):
        if speed is None:
            speed = self.speed
        self.rect.x += speed

    def update(self, game):
        print(self.state.get())
        if self.state.get() == "Jumping":
            self.rect.bottom += 1
            if self.rect.bottom == game.screen_size[1]:
                self.state.set("Idle")

    def jump(self, speed=None):
        if self.state.get() == "Jumping":
            return
        self.state.set("Jumping")
        if speed is None:
            speed = self.speed
        self.rect.y -= speed*20
