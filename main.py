import pygame 
from cell import *

GRID_WIDTH = 100
GRID_HEIGHT = 100
CELL_SIZE = 10

def main():
    # Initialize pygame
    pygame.init()
    time_clock = pygame.time.Clock()

    # Screen Dimensions - Set to system display dimensions
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w
    screen_height = screen_info.current_h
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Battle of Life")

    #Create starting grid
    grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

    #Initialize all cells in the grid to Cells
    for x in range(GRID_WIDTH-1):
        for y in range(GRID_HEIGHT-1):
            grid[x][y] = Cell(x, y, CELL_SIZE)

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #Create a second grid store the next state of the game board
        next_grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

        

        #Update the display
        pygame.display.flip()

    #Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()