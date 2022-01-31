import os
import sys
import pygame
from settings import *
from MapAPI import *
from widgets import *

pygame.init()
pygame.display.set_caption('MapAPI')
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
ButtonOut = Button(screen, 'Выход', (screen.get_width() - 180, screen.get_height() - 80), (160, 60), BLUE, BlACK)
ImagSur = Image(screen, image("37.530887", "55.703118", "0.002"), (0, 0), (screen.get_width(), screen.get_height()))

if __name__ == '__main__':
    running = True
    screen.fill((0, 0, 0))
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ButtonOut.get_button().collidepoint(event.pos):
                    running = False

        ImagSur.draw_image()
        ButtonOut.draw_button()

        pygame.display.flip()
        clock.tick(FPS)
