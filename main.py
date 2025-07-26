import pygame
from constants import (SCREEN_HEIGHT,SCREEN_WIDTH,ASTEROID_KINDS,
                       ASTEROID_MAX_RADIUS,ASTEROID_MIN_RADIUS,ASTEROID_SPAWN_RATE)

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        screen.fill((0,0,0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
