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

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

        #Update the display
        pygame.display.flip()

    #Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()