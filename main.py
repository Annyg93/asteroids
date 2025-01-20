import pygame
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    
    print(f"Starting asteroids!\n Screen width: {SCREEN_WIDTH} \n Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_active = True

    while game_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0,0,0))

        pygame.display.flip()

        dt = clock.tick(60) / 1000
        



    


if __name__ == "__main__":
    main()