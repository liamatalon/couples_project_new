import pygame

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 250
PLAYER_IMAGE = pygame.image.load(r'soldier.png')
FONT_NAME = "Calibri"
WHITE = (225, 225, 225)
BLACK = (0, 0, 0)
GREEN = (0, 179, 60)
RED = (255, 89, 94)
BLUE = (25, 130, 196)
ORANGE = (255, 202, 58)
VIOLET = (106, 76, 147)
FPS = 60

LOSE_MESSAGE = "You Lost!"
LOSE_FONT_SIZE = int(0.15 * WINDOW_WIDTH)
LOSE_COLOR = BLACK
LOSE_LOCATION = \
    (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (LOSE_FONT_SIZE / 2))
WIN_MESSAGE = "You Won!"
WIN_FONT_SIZE = LOSE_FONT_SIZE
WIN_COLOR = (89, 89, 89)
WIN_LOCATION = \
    (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (WIN_FONT_SIZE / 2))
START_MESSAGE = 'Welcome to The Flag game.\nHave Fun!'
START_MESSAGE_FONT_SIZE = LOSE_FONT_SIZE



EXPLOSION_IMAGE = pygame.image.load(r'explosion.png')
FLAG_IMAGE = pygame.image.load(r'flag.png')
GRASS_IMAGE = pygame.image.load(r'grass.png')
INJURY_IMAGE = pygame.image.load(r'injury.png')
MINE_IMAGE = pygame.image.load(r'mine.png')
SNAKE_IMAGE = pygame.image.load(r'snake.png')
SOLIDIER_NIGTH_IMAGE = pygame.image.load(r'soldier.png')