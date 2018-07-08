class Logic:
    def __init__(self, pixel_size, width, height):
        self.pixel_size = pixel_size
        self.width = width
        self.height = height
        self.grid_width = int(self.width / self.pixel_size)
        self.grid_height = int(self.height / self.pixel_size)
        self.grid = []
        self.generate_grid()

    def generate_grid(self):
        for x in range(0, self.grid_width):
            self.grid.append([])
            for y in range(0, self.grid_height):
                self.grid[x].append(0)

    def get_grid(self):
        return self.grid
