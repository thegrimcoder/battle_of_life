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
    green_button_rect = pygame.Rect(popup_x + button_spacing, popup_y + 150, button_width, button_height)
    red_button_rect = pygame.Rect(popup_x + button_spacing + button_width + button_spacing, popup_y + 150, button_width, button_height)
    blue_button_rect = pygame.Rect(popup_x + button_spacing + 2 * (button_width + button_spacing), popup_y + 150, button_width, button_height)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if green_button_rect.collidepoint(mouse_pos):
                    return 'green'
                if red_button_rect.collidepoint(mouse_pos):
                    return 'red'
                if blue_button_rect.collidepoint(mouse_pos):
                    return 'blue'

        #Draw the popup
        #Drawing a semi-transparent background to dim the main game
        s = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
        s.fill((0, 0, 0, 150))
        screen.blit(s, (0, 0))

        #Draw the popup box
        popup_rect = pygame.Rect(popup_x, popup_y, popup_width, popup_height)
        pygame.draw.rect(screen, (200, 200, 200), popup_rect)

        #Draw the buttons
        pygame.draw.rect(screen, green_button_color, green_button_rect)
        pygame.draw.rect(screen, red_button_color, red_button_rect)
        pygame.draw.rect(screen, blue_button_color, blue_button_rect)

        #Draw popup text
        font = pygame.font.Font(None, 36)
        text_surface = font.render("Choose your team:", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(popup_x +popup_width/2, popup_y + 50))
        screen.blit(text_surface, text_rect)

        #Draw text on buttons
        button_font = pygame.font.Font(None, 24)
        green_text = button_font.render("Green", True, (255, 255, 255))
        green_text_rect = green_text.get_rect(center=green_button_rect.center)
        screen.blit(green_text, green_text_rect)

        red_text = button_font.render("Red", True, (255, 255, 255))
        red_text_rect = red_text.get_rect(center=red_button_rect.center)
        screen.blit(red_text, red_text_rect)

        blue_text = button_font.render("Blue", True, (255, 255, 255))
        blue_text_rect = blue_text.get_rect(center=blue_button_rect.center)
        screen.blit(blue_text, blue_text_rect)        

        #Update display
        pygame.display.flip()