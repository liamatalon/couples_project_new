import pygame
import screen
import consts

def main():
    run = True
    main_window = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    mokesh_window = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    while run:
        clock.tick(consts.FPS)
        screen.main_window(main_window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


    pygame.quit()

def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    return run





if __name__ == '__main__':
    main()

