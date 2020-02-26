from contextlib import contextmanager


class State:

    def __init__(
                self,
                noraml_states=set(),
                unstopable_states=set(),
                default_state="Idle"):

        self.noraml_states = noraml_states
        self.unstopable_states = unstopable_states
        self.default_state = default_state

        self._state = {self.default_state: True, }
        for option in self.noraml_states | self.unstopable_states:
            if option == self.default_state:
                continue
            self._state[option] = False

    @classmethod
    def basic_state(cls):
        default_state = "Idle"
        noraml_states = {
                "Idle",
                "Emote",
                "Walk",
                "Death"}

        unstopable_states = {"Attacking",
                             "Dying",
                             "Dead"}
        return cls(noraml_states, unstopable_states, default_state)

    def get(self) -> str:
        for key, value in self._state.items():
            if value:
                return key

    def set(self, new_state, override=False):
        if ((self.get() not in self.unstopable_states and
            self.get() != new_state) or
                override):

            for key in self._state.keys():
                self._state[key] = False
            self._state[new_state] = True
<<<<<<< Updated upstream
=======

    def __repr__(self):
        return self.get()
>>>>>>> Stashed changes
