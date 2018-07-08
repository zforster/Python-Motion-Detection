import pygame
from Webcam import Webcam


class Window:
    def __init__(self):
        pygame.init()
        self.webcam = Webcam()
        self.size = self.webcam.get_size()
        self.width = self.size[0]
        self.height = self.size[1]
        self.display = pygame.display.set_mode((self.width, self.height))
        self.set_image()

    def set_image(self):
        while True:
            self.display.blit(self.webcam.get_image(), (0,0))
            pygame.display.update()

wind = Window()
