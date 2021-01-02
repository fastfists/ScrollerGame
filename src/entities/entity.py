from contextlib import contextmanager
import pygame

from .state import State


class Entity(pygame.sprite.Sprite):

    max_health = 100
    health = 100
    animation_speed = 0.15
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

    @property
    def dead(self):
        return self.state.get() == "Dead"

    def animate(self):
        """ Changes the frame of the image """
        if not self.dead:
            self.counter += self.animation_speed
            if self.counter >= 1:
                # Changes to another image/frame
                self.counter = 0
                self.frame += 2
                if self.frame > len(self.images) - 1:
                    # Resets the complete animation
                    if self.state.get() in self.state.unstopable_states:
                        if self.state.get() == "Dying":
                            self.kill()
                            self.state.set("Dead", override=True)
                        else:
                            self.state.set(self.state.default_state, override=True)
                    self.reset_animations()

    def update(self, game):
        self.animate()

    def reset_animations(self):
        """Sets the frame counters to 0"""
        self.frame, self.counter = 0, 0
