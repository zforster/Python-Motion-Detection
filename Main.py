from Window import Window
from Logic import Logic
from Webcam import Webcam

class Main:
    def __init__(self):
        self.camera = Webcam()
        self.size = self.camera.get_size()
        self.width = self.size[0]
        self.height = self.size[1]
        self.window = Window(self.width, self.height)
        self.logic = Logic(50, self.width, self.height, self.camera)
        self.grid = self.logic.get_grid()
        for line in self.grid:
            print(line)

main = Main()
