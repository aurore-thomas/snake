import pygame

#------------------------------------
#          COLORS AND FONTS
# -----------------------------------
class Colors :
    WHITE = (255, 255, 255)
    BLACK = (25, 25, 25)
    ORANGE_1 = '#EAA763'
    ORANGE_2 = '#F8C180'
    SALMON_1 = '#DE7861'
    SALMON_2 = '#F2997B'
    YELLOW_1 = '#F7D567'
    YELLOW_2 = '#FCE885'
    GREEN_1 = '#74E86B'

class Fonts :
    pygame.init()
    TITLE_FONT = pygame.font.Font('fonts/Blomberg.otf', 90)
    TITLE_2_FONT = pygame.font.Font('fonts/Blomberg.otf', 70)
    BUTTON_FONT = pygame.font.Font('fonts/Blomberg.otf', 50)
    NORMAL_FONT = pygame.font.Font('fonts/Blomberg.otf', 45)

#------------------------------------
#          FIXED VALUES
# -----------------------------------
class Values:
    SIZE = (1100, 654)
    FPS = 60
    CELL_SIZE = 30
    CELL_NUMBER = 20
    SPEED_GAME = 20