import pygame

def display_game_rules(screen):
    popup_width = 800
    popup_height = 400
    button_width = 100
    button_height = 50
    button_spacing = 20

    #Centering popup within the center of the screen
    popup_x = (screen.get_width()/2) - (popup_width/2)
    popup_y = (screen.get_height()/2) - (popup_height/2)

    #Define OK button color
    ok_button_color = (0, 0, 0)

    #Define button position for click detection
    ok_button_rect = pygame.Rect(popup_x + popup_width/2 - button_width/2, popup_y + popup_height - 75, button_width, button_height)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if ok_button_rect.collidepoint(mouse_pos):
                    return

        #Draw the popup
        #Drawing a semi-transparent background to dim the main game
        s = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
        s.fill((0, 0, 0, 150))
        screen.blit(s, (0, 0))

        #Draw the popup box
        popup_rect = pygame.Rect(popup_x, popup_y, popup_width, popup_height)
        pygame.draw.rect(screen, (200, 200, 200), popup_rect)

        #Draw the buttons
        pygame.draw.rect(screen, ok_button_color, ok_button_rect)

        #Draw popup text
        font = pygame.font.Font(None, 36)
        text_surface = font.render("Welcome To The Battle Of Life!", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(popup_x +popup_width/2, popup_y + 50))
        screen.blit(text_surface, text_rect)

        #Draw text on buttons
        button_font = pygame.font.Font(None, 24)
        ok_text = button_font.render("Ok", True, (255, 255, 255))
        ok_text_rect = ok_text.get_rect(center=ok_button_rect.center)
        screen.blit(ok_text, ok_text_rect)      

        #Draw Main Rules
        font_Rules = pygame.font.Font(None, 14)
        rules_surface = font_Rules.render("Test", True, (255, 255, 255))
        #######

        #Update display
        pygame.display.flip()