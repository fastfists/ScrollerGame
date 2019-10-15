from .entity import Entity
import pygame

class Player(Entity):

    max_energy = 100
    energy = 50
    energey_reload = 0.25

    max_health = 100
    health = 100

    speed = 1

    def move_left(speed=None):
        if speed is None:
            speed = self.speed
        self.rect.x += speed

    def move_right(speed=None):
        if speed is None:
            speed = self.speed
        self.rect.x += speed

    def draw(self, screen):
        print("hi john")
        screen.blit(self.image, self.rect)
        
    def update(self):
        if self.rect.top > 0:
            self.rect.top -=1

    def jump(self):
        self.rect.y += speed*3

