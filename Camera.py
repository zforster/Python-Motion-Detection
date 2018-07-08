import pygame.camera

class Camera:
    def __init__(self):
        pygame.camera.init()
        self.cam_list = pygame.camera.list_cameras()
        self.camera = self.cam_list[0]
        self.camera.start()

cam = Camera()
