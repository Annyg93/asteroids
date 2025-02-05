import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shoot import Shot
from scoreboard import Scoreboard
import sys


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )
    Shot.containers = (updatable, drawable, bullets)
    player = Player(x, y, PLAYER_RADIUS)
    asteroid_field = AsteroidField()
    scoreboard = Scoreboard()
  

    
    print(f"Starting asteroids!\n Screen width: {SCREEN_WIDTH} \n Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_active = True

    while game_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        pygame.Surface.fill(screen, (0,0,0))
        scoreboard.draw(screen)

        for obj in updatable:
            obj.update(dt)

        for obj in asteroids:
            if obj.collision(player):
                if player.lives >= 1:
                    player.respawn(x, y)
                else:
                    print("Game over!")
                    sys.exit()

            for bullet in bullets:
                if obj.collision(bullet):
                    obj.split()
                    bullet.kill()
                    scoreboard.add_points(10)

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000
        



    


if __name__ == "__main__":
    main()