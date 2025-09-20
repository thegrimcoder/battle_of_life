import pygame
import random
from cell import *
from player_choice import *
from game_rules import *

GRID_WIDTH = 25
GRID_HEIGHT = 25
CELL_SIZE = 20
PLAYER_TEAM = None
COMPUTER_TEAM = None

#SCREEN_RATIO = 1
#SCREEN_WIDTH_OFFSET = 0
#SCREEN_HEIGHT_OFFSET = 0

def draw_grid(screen, grid):
    #Clear Screen
    screen.fill((0, 0, 0))

    #Iterate through the grid
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            cell = grid[x][y]

            #Checking if the Cell is alive - obtaining appropriate color
            if cell.get_alive():
                color = cell.get_color()
            else:
                color = (255, 255, 255)

            #Calculate cell position based on screen size
            rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            #rect = pygame.Rect(x*CELL_SIZE*SCREEN_RATIO+SCREEN_WIDTH_OFFSET, y*CELL_SIZE*SCREEN_RATIO+SCREEN_HEIGHT_OFFSET, CELL_SIZE*SCREEN_RATIO+SCREEN_WIDTH_OFFSET, CELL_SIZE*SCREEN_RATIO+SCREEN_HEIGHT_OFFSET)

            #Draw the cell
            pygame.draw.rect(screen, color, rect)

            #Draw a border around the cell
            pygame.draw.rect(screen, (0,0,0), rect, 1)

def main():
    #Initialize pygame
    pygame.init()
    time_clock = pygame.time.Clock()

    #Screen Dimensions - Set to system display dimensions
    #screen_info = pygame.display.Info() - Do I need this or should I use the width and height of the grid???
    screen_width = GRID_WIDTH*CELL_SIZE
    screen_height = GRID_HEIGHT*CELL_SIZE

    #Update screen ratio based on dynamic screen size
    #global SCREEN_RATIO
    #SCREEN_RATIO = screen_width/screen_height
    
    #Update screen offset based on dynamic screen size - centers grid
    #grid_screen_width = GRID_WIDTH*CELL_SIZE
    #grid_screen_height = GRID_HEIGHT*CELL_SIZE

    #global SCREEN_WIDTH_OFFSET
    #SCREEN_WIDTH_OFFSET = (screen_width-grid_screen_width)/2

    #global SCREEN_HEIGHT_OFFSET
    #SCREEN_HEIGHT_OFFSET = 10

    screen = pygame.display.set_mode((screen_width, screen_height), pygame.SCALED)
    pygame.display.set_caption("Battle of Life")

    #Create starting grid
    grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

    #Create a second grid store the next state of the game board
    next_grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

    #Initialize all cells in both grids to dead Cells
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            grid[x][y] = Cell(x, y, CELL_SIZE)
            next_grid[x][y] = Cell(x, y, CELL_SIZE)

    #Draw Initial Window
    pygame.display.flip()

    #Draw Initial Grid
    draw_grid(screen, next_grid)

    #Display game rules
    display_game_rules(screen)

    #Prompt user for team choice
    global PLAYER_TEAM
    PLAYER_TEAM = get_player_choice(screen)

    #Computer Player Choice - Psuedo random - Coin flip between remaining teams
    rand_int = random.randint(1,2)
    match PLAYER_TEAM:
        case 'green':
            match rand_int:
                case 1:
                    COMPUTER_TEAM = 'red'
                case 2:
                    COMPUTER_TEAM = 'blue'
        case 'red':
            match rand_int:
                case 1:
                    COMPUTER_TEAM = 'green'
                case 2:
                    COMPUTER_TEAM = 'blue'
        case 'blue':
            match rand_int:
                case 1:
                    COMPUTER_TEAM = 'green'
                case 2:
                    COMPUTER_TEAM = 'red'

    print(f"Player Team: {PLAYER_TEAM}\n")
    print(f"Computer Team: {COMPUTER_TEAM}\n")

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #Draw Grid
        draw_grid(screen, next_grid)

        #Update the display
        pygame.display.flip()

    #Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()



            