import sys
import random
from settings import *

# ------------------------------------
#               WINDOW
# ------------------------------------
# We define the game window. We can't put all this in a function because of the class Fonts,
# which need pygame.init() to work. 
pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode(Values.SIZE)
pygame.display.set_caption("Snake game")


# ------------------------------------
#               BUTTONS  
# ------------------------------------
def text_objects(text, font):
    # We create the style of the text button, then we return it and its size (in a rectangle)
    text_surface = font.render(text, True, Colors.WHITE)
    return text_surface, text_surface.get_rect()

def button(text, x, y, w, h, ic, ac, action=None):
    # ic is for inactive color, ac is for active color
    mouse = pygame.mouse.get_pos() # It gives us information about the mouse's position
    click = pygame.mouse.get_pressed() # It gives information about the number of click

    # When mouse hovers the button, active color change to inactive color
    # We use the mouse's position to know if the cursor is on the button or not
    if (x + w) > mouse[0] > x and (y + h) > mouse[1] > y:
        pygame.draw.rect(win, ac, (x, y, w, h), border_radius=10)

        # If action isn't given in the parameters, click on the button won't do anything
        if click[0] == 1 and action != None:
            action()

    else:
        # Button with the inactive color : 
        pygame.draw.rect(win, ic, (x, y, w, h), border_radius=10)

    text_surf, text_rect = text_objects(text, Fonts.BUTTON_FONT)
    text_rect.center = ((x + (w/2)), (y + (h/2))) # To have the text in the middle of the button
    win.blit(text_surf, text_rect)

# ------------------------------------
#              MAIN MENU
# ------------------------------------
def main_menu():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# ------------------------------------
#              SCORES PAGE
# ------------------------------------
def scores():
    pass

# ------------------------------------
#               GAME
# ------------------------------------
def game():
    running = True

    # Background :
    menu_background = pygame.image.load("pictures/background.png")
    win.blit(menu_background, (0,0))

    game_surface = pygame.Surface((Values.CELL_SIZE * Values.CELL_NUMBER, Values.CELL_SIZE * Values.CELL_NUMBER))



    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        win.blit(game_surface, (40, 25))
        
        pygame.display.update()
        clock.tick(Values.FPS)


# ------------------------------------
#               ENDGAME
# ------------------------------------
def endgame():
    pass

# ------------------------------------
#                 MAIN
# ------------------------------------

def main():
    running = True

    # Background :
    menu_background = pygame.image.load("pictures/background.png")
    win.blit(menu_background, (0,0))

    # Title :
    title = Fonts.TITLE_FONT.render("SNAKE GAME", True, Colors.BLACK)
    title_rect = title.get_rect(center=(Values.SIZE[0]/2, 200))
    win.blit(title, title_rect)


    while running:
        # Buttons : (we have to draw them here because of the hover)
        button("PLAY", 450, 300, 200, 70, Colors.ORANGE_2, Colors.ORANGE_1, game)
        button("SCORES", 450, 400, 200, 70, Colors.ORANGE_2, Colors.SALMON_2, action=None)
        button("QUIT", 450, 500, 200, 70, Colors.ORANGE_2, Colors.YELLOW_2, quit)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()
        clock.tick(Values.FPS)

main()