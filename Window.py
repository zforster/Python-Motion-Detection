import pygame
from Webcam import Webcam


class Window:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))

    def get_display(self):
        return self.display
