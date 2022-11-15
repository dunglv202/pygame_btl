from pygame import Surface
from gui.button import Button

class SimpleMenu(Surface):
    def __init__(self, width: int, height: int, button_spacing: int):
        super().__init__((width, height))
        self.fill("ORANGE")
        self.button_spacing = button_spacing
        self.bottom = 0
        self.button_list = list()

    def add_button(self, button: Button):
        self.button_list.append(button)
        button.rect = button.get_rect(midtop = (self.get_width()/2, self.bottom))
        self.blit(button.convert_alpha(), button.rect)
        self.bottom += button.get_height() + self.button_spacing

    def handle_click(self, cursor_pos):
        for button in self.button_list:
            if button.onclick != None and button.rect.collidepoint(cursor_pos):
                button.click()