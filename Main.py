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
        loop_no = 0
        got_two = False
        grid_even = []
        grid_odd = []
        while True:
            if(loop_no % 2 == 0):
                self.logic.generate_grid()
                grid_even = self.logic.get_grid()
                #self.window.show_image(grid_even, self.pixel_size)
                self.window.show_raw_image(self.camera.get_image())
            else:
                self.logic.generate_grid()
                grid_odd = self.logic.get_grid()
                #self.window.show_image(grid_odd, self.pixel_size)
                self.window.show_raw_image(self.camera.get_image())
                if(loop_no > 2):
                    position = self.logic.compare_grids(grid_even, grid_odd)
                    if(not(position == None)):
                        self.window.draw_location(grid_odd, position, self.pixel_size)
            loop_no = loop_no + 1
            if(loop_no > 10000):
                loop_no = 0

main = Main()
