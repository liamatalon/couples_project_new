import pygame
from pygame.locals import *
import consts
import os


main_window = pygame.display.set_mode(
                (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

mokesh_window = pygame.display.set_mode(
                (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def main_window(window):
        pygame.display.set_caption('Player Movement')
        window.fill(consts.GREEN)
        return window

def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)

def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)

def draw_start_message():
    draw_message()
    pass

def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    main_window.blit(text_img, location)

pygame.display.update()
