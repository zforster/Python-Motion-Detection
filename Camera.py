import pygame.camera

class Camera:
    def __init__(self):
        pygame.camera.init()
        self.cam_list = pygame.camera.list_cameras()
        self.webcam = self.cam_list[0]
        self.webcam.start()

    def get_image(self):
        return self.camera.get_image()

cam = Camera()
cam.get_image()
