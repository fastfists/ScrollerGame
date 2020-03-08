import pygame
from contextlib import contextmanager


class Character(pygame.sprite.Sprite):
    """
    The sprite abstract class
    handles the animation and changing
    of states for a sprite object
    """
    max_health = 100
    health = 100
    possible_states = {"Idle",
                       "Emote",
                       "Walk",
                       "Death"}
    default_state = "Idle"
    animation_speed = 1
    speed = 0.5
    frame = 0
    counter = 0
    unstopable_states = {"Attacking",
                         "Dying",
                         "Dead"}
    _end = False

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # create the _state instance
        self._state = {self.default_state: True}
        for option in self.possible_states | self.unstopable_states:
            if option == self.default_state:
                continue
            self._state[option] = False
        if not hasattr(self, "_images"):
            self._images = utils.get_all_images(self.__class__.__name__)  # returns a dict
        self._images["Dead"] = [self._images["Dying"][-1]]  # passes the last index

    def __init_subclass__(cls, picture_name: str = None, **kwargs):
        if picture_name:
            cls._images = utils.get_all_images(picture_name)
        super().__init_subclass__(**kwargs)

    def animate(self):
        """ Changes the frame of the image """
        if not self.dead:
            self.counter += self.animation_speed
            if self.counter >= 1:
                # Changes to another image/frame
                self.counter = 0
                self.frame += 1
                if self.frame > len(self.images) - 1:
                    # Resets the current animation
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

    @property
    def dead(self):
        return self.state == "Dead"

    def on_death(self):
        pass

    @contextmanager
    def end_of_animation(self):
        self._end = True
        yield
        self._end = False

    def reset_animations(self):
        """Sets the frame counters to 0"""
        self.frame, self.counter = 0, 0

    def damage(self, dmg):
        """ Reduces the health"""
        self.health -= dmg
        if self.health <= 0:
            self.state = "Dying"
            self.on_dying()

    def on_dying(self):
        pass

    @property
    def state(self) -> str:
        for key, value in self._state.items():
            if value:
                return key

    @state.setter
    def state(self, new_state):
        if (self.state not in self.unstopable_states and self.state != new_state) or self._end:
            self.reset_animations()
            for key in self._state.keys():
                self._state[key] = False
            self._state[new_state] = True

    @property
    def images(self):
        return self._images[self.state]

    @property
    def image(self) -> pygame.surface.Surface:
        return self.images[self.frame]

    def __repr__(self):
        return f"{self.__class__.__name__} object at pos: {self.x}, {self.y} currently {self.state}"
