from contextlib import contextmanager
import pygame

from .state import State


class Entity(pygame.sprite.Sprite):

    max_health = 100
    health = 100
    animation_speed = 1
    frame = 0
    counter = 0
    state = State.basic_state()

    def __init__(
            self,
            *,
            image_ref=None,
            rect=None,
            bbox=None,
            state: State=None,
            **options):
        """
        images = {
            state1 : [ pygame.Surface(), ...],
            ...
        }
        """
        super().__init__()
        self.image_ref = image_ref
        self.state = state
        self.rect = rect
        self.bbox = bbox or self.rect
        self.configure_options(**options)

    def configure_options(self, **options):
        for key, value in options.items():
            exec(f"self.{key} = value")

    @property
    def image(self):
        return self.image_ref[self.state.get()][self.frame]

    @property
    def images(self):
        return self.image_ref[self.state.get()]

    def animate(self):
        """ Changes the frame of the image """
        if not self.dead:
            self.counter += self.animation_speed
            if self.counter >= 1:
                # Changes to another image/frame
                self.counter = 0
                self.frame += 1
                if self.frame > len(self.images) - 1:
                    # Resets the complete animation
                    if self.state.get() in self.unstopable_states:
                        if self.state == "Dying":
                            self.kill()
                            with self.end_of_animation():
                                self.state = "Dead"
                                self.on_death()
                        else:
                            with self.end_of_animation():
                                self.state = self.default_state
                    self.reset_animations()

    def update(self, game):
        self.animate()

    def reset_animations(self):
        """Sets the frame counters to 0"""
        self.frame, self.counter = 0, 0
