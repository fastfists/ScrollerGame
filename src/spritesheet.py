import pygame
from src import settings

SkeletonSheet = None
RougeSheet = None


class SpriteSheet:

    def __init__(self, file_name, states: list, frame_max, size: tuple=None):
        """
            Receives the file name and a list of states in order.
            Each state needs to be on the same line
        """

        self.sheet = pygame.image.load(file_name)
        self.states = states
        self.size = size
        self.frame_max = frame_max

    def process(self):
        ref_dict = {}

        for state in self.states:
            ref_dict[state] = []
            for frame in range(self.frame_max):
                ref_dict[state].append(self.get_image_from_state(state, frame))

        return ref_dict

    def get_image_from_state(self, state, framenum):

        if not self.size:
            raise AssertionError("Needs a size to be specified")

        statenum = self.states.index(state)

        x = framenum * self.size[0]
        y = statenum * self.size[1]

        return self.get_image_from_pix(x, y, self.size)

    def get_image_from_pix(self, x, y, size: tuple=None):

        if not size:
            size = self.size

        image = pygame.Surface(size).convert()
        image.blit(self.sheet, (0, 0), ((x, y), size))
        image.set_colorkey((0, 0, 0))

        return image

    def __str__(self):
        return self.sheet


def init_spritesheet():
    global SkeletonSheet
    global RougeSheet

    SkeletonSheet = SpriteSheet(settings.img_direc + "skeleton.png", states=['Idle', 'Jumping', 'Walking', 'Attacking', 'Dying'], frame_max=10, size=(20, 32))
    RougeSheet = SpriteSheet(settings.img_direc + "rouge.png", states=['Idle', 'Jumping', 'Walking', 'Attacking', 'Dying'], frame_max=10, size=(20, 32))
