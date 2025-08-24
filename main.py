import pygame
import screen
import consts

def main():
    run = True
    main_window = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

    mokesh_window = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    while run:
        screen.main_window(main_window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


    pygame.quit()







if __name__ == '__main__':
    main()

