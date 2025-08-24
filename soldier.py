import pygame
import consts
import screen


def resize_soldier():
    from PIL import Image
    SOLDIER_IMAGE_or = consts.SOLDIER_IMAGE_origin
    print(f"Original size : {SOLDIER_IMAGE_or.size}") # 5464x3640
    SOLDIER_IMAGE_resized = SOLDIER_IMAGE_or.resize((100, 100))
    SOLDIER_IMAGE_resized.save('soldier_100.jpeg')
    SOLDIER_IMAGE = pygame.image.load(r'soldier_100.png')
    return SOLDIER_IMAGE

def soldier_location():
    SOLDIER_IMAGE = resize_soldier()
    screen.main_window.blit(SOLDIER_IMAGE, (consts.x, consts.y))
