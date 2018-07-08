from Window import Window
from Logic import Logic
from Webcam import Webcam

class Main:
    def __init__(self):
        self.pixel_size = 20
        self.camera = Webcam()
        self.size = self.camera.get_size()
        self.width = self.size[0]
        self.height = self.size[1]
        self.window = Window(self.width, self.height)
        self.logic = Logic(self.pixel_size, self.width, self.height, self.camera)
        self.run()
        
    def run(self):
        while True:
            self.logic.generate_grid()
            self.grid = self.logic.get_grid()
            self.window.show_image(self.grid, self.pixel_size)

main = Main()
