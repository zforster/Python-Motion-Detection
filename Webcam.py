import pygame.camera

class Webcam:
    def __init__(self):
        pygame.camera.init()
        self.cam_list = pygame.camera.list_cameras()
        self.webcam = pygame.camera.Camera(self.cam_list[0])
        self.webcam.start()

    def get_image(self):
        return self.webcam.get_image()

    def get_size(self):
        return self.webcam.get_size()
    
