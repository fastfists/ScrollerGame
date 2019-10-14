import pygame
from contextlib import contextmanager

class State():

    @classmethod
    def basic_state(cls):

        default_state = "Idle"
        possible_states = {"Idle",
                           "Emote",
                           "Walk",
                           "Death"}

        unstopable_states = {"Attacking",
                             "Dying",
                             "Dead"}
        return cls(possible_states, unstopable_states, default_state)

    def __init__(self, possible_states, unstopable_states, default_state="Idle"):
        self.possible_states = possible_states
        self.unstopable_states = unstopable_states
        self.default_state = default_state

        self._state = {self.default_state: True}
        for option in self.possible_states | self.unstopable_states:
            if option == self.default_state:
                continue
            self._state[option] = False

    @contextmanager
    def end_of_animation(self):
        self._end = True
        yield
        self._end = False

    def get(self) -> str:
        for key, value in self._state.items():
            if value:
                return key

    def set(self, new_state, override=False):
        if (self.get() not in self.unstopable_states and self.get() != new_state) or override:
            for key in self._state.keys():
                self._state[key] = False
            self._state[new_state] = True

class Player(pygame.sprite.Sprite):

    max_health = 100
    health = 100
    animation_speed = 1
    frame = 0
    counter = 0

    def __init__(self, image_ref: dict, state: State):
        """
        images = {
            state1 : [ pygame.Surface(), ...],
            ...
        }
        """
        self.image_ref = image_ref
        self.state = state

    @property
    def image(self):
        return self.image_ref[self.state.get()][self.frame]

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
                    if self.state in self.unstopable_states:
                        if self.state == "Dying":
                            super().kill()
                            with self.end_of_animation():
                                self.state = "Dead"
                                self.on_death()
                        else:
                            with self.end_of_animation():
                                self.state = self.default_state
                    self.reset_animations()

    def reset_animations(self):
        """Sets the frame counters to 0"""
        self.frame, self.counter = 0, 0
