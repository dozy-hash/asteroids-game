import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for thing in updatable:
            thing.update(dt)
        
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()
        
        screen.fill("black")
            
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()