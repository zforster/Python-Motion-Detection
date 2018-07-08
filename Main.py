from Window import Window
from Logic import Logic
from Webcam import Webcam

class Main:
    def __init__(self):
        self.camera = Webcam()
        self.size = self.camera.get_size()
        self.width = self.size[0]
        self.height = self.size[1]
        self.logic = Logic(10, self.width, self.height)
        print(self.logic.get_grid())

main = Main()
