import pygame

def get_player_choice(screen):
    popup_width = 400
    popup_height = 300
    button_width = 100
    button_height = 50
    button_spacing = 20

    #Centering popup within the center of the screen
    popup_x = (screen.get_width()/2) - (popup_width/2)
    popup_y = (screen.get_height()/2) - (popup_height/2)

    #Define button colors
    green_button_color = (0, 255, 0)
    red_button_color = (255, 0, 0)
    blue_button_color = (0, 0, 255)

    #Define button position for click detection
    green_button_rect = pygame.Rect(popup_x + button_spacing, popup_y + button_spacing, button_width, button_height)
    red_button_rect = pygame.Rect(popup_x + button_spacing + button_width + button_spacing, popup_y + 150, button_width, button_height)
    blue_button_rect = pygame.Rect(popup_x + button_spacing + 2 * (button_width + button_spacing), popup_y + 150, button_width, button_height)

    #Draw the popup
    #Drawing a semi-transparent background to dim the main game
    s = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
    s.fill((0, 0, 0, 150))
    screen.blit(s, (0, 0))

    #Draw the popup box
    popup_rect = pygame.Rect(popup_x, popup_y, popup_width, popup_height)
    pygame.draw.rect(screen, (200, 200, 200), popup_rect)

    #Update display
    pygame.display.flip()