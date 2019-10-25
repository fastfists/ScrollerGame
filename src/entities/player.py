from .entity import Entity
import pygame


class Player(Entity):

    max_energy = 200
    energy = 200
    energy_reload = 0.1
    base_energy_reload = 0.005
    energy_accel = 0.005

    max_health = 100
    health = 100

    gravity = 1
    y_vel = 0
    speed = 7

    def use_energy(self, energy_ammount):
        self.energy_reload = self.base_energy_reload
        self.energy -= energy_ammount
        if self.energy <= 1:
            self.energy += energy_ammount
            return True

    def move(self, speed=None):
        if self.use_energy(1): return
        speed = speed or self.speed
        self.rect.x += speed

    def move_left(self, speed=None):
        speed = speed or self.speed
        self.move(-abs(speed))

    def move_right(self, speed=None):
        speed = speed or self.speed
        self.move(abs(speed))

    def update(self, game):
        # super().update(game)
        touching_walls = pygame.sprite.spritecollideany(self, game.walls)
        if self.state.get() == "Jumping":
            self.y_vel += self.gravity
            self.rect.y += self.y_vel

            if touching_walls  and self.y_vel > 0:
                self.state.set("Idle", override=True)
                self.rect.bottom = touching_walls.rect.top + 1
                print(touching_walls.rect, self.rect.bottomleft)

        if self.energy < self.max_energy:
            self.energy_reload += self.energy_accel
            self.energy += self.energy_reload

        if not touching_walls :
            self.state.set("Jumping")

        touching_mobs = pygame.sprite.spritecollideany(self, game.enemies)
        if touching_mobs:
            self.damage(2)

    def damage(self, health_ammount):
        self.health -= health_ammount

    def jump(self):
        if self.state.get() == "Jumping":
            return

        if self.use_energy(3): return
        self.y_vel = -self.speed*2
        self.state.set("Jumping", override=True)
        self.jump_start = self.rect.bottom


