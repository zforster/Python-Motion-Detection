import pygame


class Logic:
    def __init__(self, pixel_size, width, height, camera):
        pygame.init()
        self.camera = camera
        self.pixel_size = pixel_size
        self.width = width
        self.height = height
        self.grid_width = int(self.width / self.pixel_size)
        self.grid_height = int(self.height / self.pixel_size)
        self.grid = []

    def generate_grid(self):
        image = self.camera.get_image()
        self.grid = []
        for x in range(0, self.grid_width):
            self.grid.append([])
            for y in range(0, self.grid_height):
                rect = pygame.draw.rect(image, (255,255,255), (x * self.pixel_size, y * self.pixel_size, self.pixel_size, self.pixel_size), 1)
                avg = pygame.transform.average_color(image, rect)
                grey = (avg[0] + avg[1] + avg[2]) / 3
                self.grid[x].append((grey,grey,grey))

    def get_grid(self):
        return self.grid

    def compare_grids(self, grid_even, grid_odd):
        for x in range(0,len(grid_even)):
            for y in range(0,len(grid_even[x])):
                even = grid_even[x][y][0] + grid_even[x][y][1] + grid_even[x][y][2]
                odd = grid_odd[x][y][0] + grid_odd[x][y][1] + grid_odd[x][y][2]
                if((even - odd < 20 or even - odd > -20)):
                    print("diff")
