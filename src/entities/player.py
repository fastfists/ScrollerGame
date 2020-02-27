from .entity import Entity
from .state import State
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
    speed = 4
    jump_speed = 20

    @classmethod
    def basic_player(cls, game):
        state = State(
                noraml_states={"Idle", "Walking"},
                unstopable_states={"Jumping"})

        size = 16, 16*2
        surface = pygame.Surface(size)
        surface.fill((255, 0, 0))

        rect = surface.get_rect()
        image_ref = {
                "Idle": [surface],
                "Jumping": [surface],
                "Walking": [surface]}

        return cls(state=state, image_ref=image_ref, rect=rect)

    def use_energy(self, energy_ammount):
        self.energy_reload = self.base_energy_reload
        self.energy -= energy_ammount
        if self.energy <= 1:
            self.energy += energy_ammount
            return True

    def walk(self, speed=None):
        speed = speed or self.speed
        self.rect.x += speed / 2

    def walk_left(self, speed=None):
        speed = speed or self.speed
        self.walk(-abs(speed))

    def walk_right(self, speed=None):
        speed = speed or self.speed
        self.walk(abs(speed))

    def run(self, speed=None):
        if self.use_energy(1):
            return
        speed = speed or self.speed
        self.rect.x += speed

    def run_left(self, speed=None):
        speed = speed or self.speed
        self.run(-abs(speed))

    def run_right(self, speed=None):
        speed = speed or self.speed
        self.run(abs(speed))

    def update(self, game):
        # super().update(game)
        touching_walls = pygame.sprite.spritecollideany(self, game.walls)
        if self.state.get() == "Jumping":
            if (touching_walls and
                    self.y_vel > 0):

                platform_top = touching_walls.rect.top

                if ((self.rect.bottom - self.y_vel) <= platform_top):

                    self.state.set("Idle", override=True)
                    self.y_vel = 0
                    self.rect.bottom = touching_walls.rect.top + 1

            self.y_vel += self.gravity
            self.rect.y += self.y_vel
        else:
            if (not touching_walls or
                    (self.rect.bottom - touching_walls.rect.top) > 2):

                self.state.set("Jumping")

        if self.energy < self.max_energy:
            self.energy_reload += self.energy_accel
            self.energy += self.energy_reload

        touching_mobs = pygame.sprite.spritecollideany(self, game.enemies)
        if touching_mobs:
            self.damage(2)

    def damage(self, health_ammount):
        self.health -= health_ammount

    def jump(self):
        if self.state.get() == "Jumping":
            return
        if self.use_energy(3):
            return
        self.y_vel = -self.jump_speed
        self.state.set("Jumping", override=True)
        self.jump_start = self.rect.bottom
