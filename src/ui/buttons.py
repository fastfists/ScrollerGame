import pygame

class Clickable():

    def __init__(self, rect, *actions_on_click):
        pygame.sprite.Sprite.__init__(self)
        self.actions = list(actions_on_click)
        self.pressed = False

    def update(self, mouse_clicked: bool):
        mouse_pos = pygame.mouse.get_pos()
        self.pressed = False
        if self.rect.collidepoint(mouse_pos):
            if not mouse_clicked:
                self.on_hover()
            else:
                self.pressed = True
                for action in self.actions:
                    action()
        else:
            self.off_hover()

    def add_action(self, action) -> None:
        self.actions.append(action)

    def on_hover(self):
        pass

    def off_hover(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} object at ({self.rect.x}, {self.rect.y}) pressed {self.pressed}"


class TextButton(Clickable):

    def __init__(self, pos:tuple, message:str, font=utils.bold_font, *actions_on_click):
        self.message = message
        self.color = (255, 255, 255)
        self.font = font
        self.image = self.font.render(self.message, True, self.color)
        size = self.text.get_rect().size
        super().__init__(pos, size, *actions_on_click)

    def update(self, mouse_clicked):
        self.image = self.font.render(self.message, True, self.color)
        super().update(mouse_clicked)

