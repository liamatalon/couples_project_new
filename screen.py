import pygame
from pygame.locals import *
import consts
import os
import soldier
import random


main_window = pygame.display.set_mode(
                (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption('Player Movement')
main_window.fill(consts.GREEN)
pygame.display.update()

mokesh_window = pygame.display.set_mode(
                (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)

def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)

def draw_start_message():
    draw_message(consts.START_MESSAGE, consts.START_MESSAGE_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)
    pass

def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    main_window.blit(text_img, location)

def draw_grass():
    grass_count = 0
    while grass_count < 20:
        image = consts.GRASS_IMAGE
        grass = pygame.transform.scale(image, (30, 30))
        ran_x = random.randrange(1, consts.WINDOW_WIDTH)
        ran_y = random.randrange(1, consts.WINDOW_HEIGHT)
        main_window.blit(grass, (ran_x, ran_y))
        grass_count += 1

def draw_soldier():
    image = soldier.soldier_image()
    main_window.blit(image, (0,0))



def draw_window():
    pygame.display.set_caption('Player Movement')
    main_window.fill(consts.GREEN)
    draw_soldier()
    draw_grass()
    pygame.display.update()


pygame.display.update()
