import pygame
from pygame.locals import *
import consts
main_window = pygame.display.set_mode(
                (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def create_window(window):
        pygame.display.set_caption('Player Movement')
        window.fill(consts.GREEN)
        return window


pygame.display.set_caption('Player Movement')

image = pygame.image.load(r'soldier.png')



pygame.display.update()
