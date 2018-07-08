import pygame


class Window:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))

    def show_image(self, grid, pixel_size):
        for x in range(0, len(grid)):
            for y in range(0, len(grid[x])):
                pygame.draw.rect(self.display, grid[x][y], (x * pixel_size,y * pixel_size, pixel_size, pixel_size))
        pygame.display.update()
        self.check_quit()

    def check_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                
    def get_display(self):
        return self.display
