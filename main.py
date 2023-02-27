import sys
import random
from settings import *

# ------------------------------------
#               WINDOW
# ------------------------------------
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
#              SCORES PAGE
# ------------------------------------
def scores():
    pass

# ------------------------------------
#           INPUT USERNAME
# ------------------------------------
def window_game():
    running = True
    username = ""

    while running:
        # Because of the input, we have to draw all the element in the loop,
        # even the title and the buttons. Otherwise, the background will appear over them.

        # Background :
        menu_background = pygame.image.load("pictures/background.png")
        win.blit(menu_background, (0,0))

        # Title :
        title = Fonts.TITLE_2_FONT.render("SNAKE GAME", True, Colors.ORANGE_2)
        win.blit(title, (700, 50))

        # Game surface : 
        game_surface = pygame.draw.rect(win, Colors.BLACK, pygame.Rect(40, 27, Values.CELL_SIZE * Values.CELL_NUMBER, Values.CELL_SIZE * Values.CELL_NUMBER))

        # Text explanation:
        text_1 = Fonts.NORMAL_FONT.render("Enter your name", True, Colors.WHITE)
        text_2 = Fonts.NORMAL_FONT.render("and press Enter", True, Colors.WHITE)
        win.blit(text_1, (709.5, 200))
        win.blit(text_2, (709.5, 250))

        # Input : 
        text_surface = Fonts.NORMAL_FONT.render(username, False, Colors.WHITE)
        win.blit(text_surface, (870 - text_surface.get_width()/2, 320))

        # Buttons : 
        button("MENU", 770, 450, 200, 70, Colors.ORANGE_2, Colors.ORANGE_1, main)
        button("QUIT", 770, 550, 200, 70, Colors.SALMON_2, Colors.SALMON_1, quit)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                elif event.key == pygame.K_RETURN:
                    print(username)
                    play(username)
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                else:
                    username += event.unicode # To write with the keyboard

        

        pygame.display.update()
        # clock.tick(Values.FPS)

# ------------------------------------
#           INPUT USERNAME
# ------------------------------------
    
def play(username):
    running = True
    game_over = False
    score = 0

    menu_background = pygame.image.load("pictures/background.png")
    win.blit(menu_background, (0,0))

    # Title :
    title = Fonts.TITLE_2_FONT.render("SNAKE GAME", True, Colors.ORANGE_2)
    win.blit(title, (700, 50))

    # Username display :
    display_username = Fonts.NORMAL_FONT.render(" PLAYER : " + username + " ", True, Colors.BLACK)
    pygame.draw.rect(win, Colors.SALMON_1, pygame.Rect(870 - display_username.get_width()/2, 146, display_username.get_width(), 50), border_radius= 10)
    win.blit(display_username, (870 - display_username.get_width()/2, 150))

    # Initial position in the middle of the game surface :
    snake_position = [320, 309] 
    direction = "west" # Initial move

    # Fruits : 
    fruit_apparition = [random.randrange(50, 630), random.randrange(37, 617) ]
    fruit_is_present = True

    while running:
        snake = [ [snake_position[0], snake_position[1]], 
                [snake_position[0], snake_position[1]],
                [snake_position[0], snake_position[1]] ]

        # Display elements :
        game_surface = pygame.draw.rect(win, Colors.BLACK, pygame.Rect(40, 27, Values.CELL_SIZE * Values.CELL_NUMBER, Values.CELL_SIZE * Values.CELL_NUMBER))
        button("FINISH", 770, 450, 200, 70, Colors.ORANGE_2, Colors.ORANGE_1)
        button("MENU", 770, 550, 200, 70, Colors.SALMON_2, Colors.SALMON_1, main)
        display_score(score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # To change direction :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction = "north"
                elif event.key == pygame.K_DOWN:
                    direction = "south"
                elif event.key == pygame.K_RIGHT:
                    direction = "east"
                elif event.key == pygame.K_LEFT:
                    direction = "west"
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            
        # The snake has to move constantly : 
        if direction == "north":
            snake_position[1] -= Values.CELL_SIZE
        elif direction == "south":
            snake_position[1] += Values.CELL_SIZE
        elif direction == "east":
            snake_position[0] += Values.CELL_SIZE
        elif direction == "west":
            snake_position[0] -= Values.CELL_SIZE


        if snake_position[0] < 39 or snake_position[0]>= 619:
            print("game over")
            endgame(username, score)
        elif snake_position[1] <= 28 or snake_position[1] >= 606:
            print("game over")
            endgame(username, score)

        # Display the fruit : 
        pygame.draw.rect(win, Colors.GREEN_1, pygame.Rect(fruit_apparition[0], fruit_apparition[1], 20, 20))

        # When the snake eats the fruit :
        snake.insert(0, list(snake_position)) 
        if snake_position[0] == fruit_apparition[0] and snake_position[1] == fruit_apparition[1]:
            score += 20
            print("win")
            
            fruit_is_present = False
        # else:
        #     snake.pop()


        # If no fruit on the board : 
        if fruit_is_present == False:
            fruit_apparition = [random.randrange(50, 630), random.randrange(37, 617) ]

        # Display the snake : 
        # snake.insert(0, list(snake_position))
        for element in snake:
            pygame.draw.rect(win, Colors.YELLOW_2, pygame.Rect(element[0], element[1], Values.CELL_SIZE, Values.CELL_SIZE))

        pygame.display.update()
        clock.tick(Values.SPEED_GAME)

# ------------------------------------
#            DISPLAY_SCORE
# ------------------------------------

def display_score(actual_score):
    score = Fonts.NORMAL_FONT.render(" Score : " + str(actual_score) + " ", True, Colors.BLACK)
    pygame.draw.rect(win, Colors.SALMON_1, pygame.Rect(870 - score.get_width()/2, 216, score.get_width(), 50), border_radius= 10)
    win.blit(score, (870 - score.get_width()/2, 220))


# ------------------------------------
#               ENDGAME
# ------------------------------------
def endgame(username, score):
    running = True
    player = username
    final_score = score
    print("Endgame")

    game_over = Fonts.TITLE_FONT.render("GAME OVER", True, Colors.ORANGE_2)
    game_over_rect = game_over.get_rect(center=(320, 309))
    win.blit(game_over, game_over_rect)

    while running:

        button("PLAY AGAIN", 745, 350, 250, 70, Colors.ORANGE_2, Colors.ORANGE_1, window_game)
        button("MENU", 770, 450, 200, 70, Colors.SALMON_2, Colors.SALMON_1, main)
        button("QUIT", 770, 550, 200, 70, Colors.SALMON_2, Colors.SALMON_1, quit)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()


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
        # Buttons : (we have to draw them in the loop because of the hover)
        button("PLAY", 450, 300, 200, 70, Colors.ORANGE_2, Colors.ORANGE_1, window_game)
        button("SCORES", 450, 400, 200, 70, Colors.ORANGE_2, Colors.SALMON_2, action=None)
        button("QUIT", 450, 500, 200, 70, Colors.ORANGE_2, Colors.YELLOW_2, quit)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    window_game()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            
        
        pygame.display.update()
        clock.tick(Values.FPS)

main()