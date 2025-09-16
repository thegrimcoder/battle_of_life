import pygame

def main():
    # Initialize pygame
    pygame.init()
    time_clock = pygame.time.Clock()

    # Screen Dimensions
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Battle of Life")

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        #Update the display
        pygame.display.flip()

    #Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()