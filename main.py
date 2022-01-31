import pygame
from settings import *

pygame.init()
pygame.display.set_caption('MapAPI')
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)

if __name__ == '__main__':
    running = True
    screen.fill((0, 0, 0))
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(FPS)
