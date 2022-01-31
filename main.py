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
lon = "37.530887"
lat = "55.703118"
delta = "0.002"
ImagSur = Image(screen, image(lon, lat, delta), (0, 0), (screen.get_width(), screen.get_height()))

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
            if pygame.event == pygame.K_PAGEUP:
                delta = f'{int(delta) - 0.001}'
                ImagSur.set_image(image(lon, lat, delta))
            if pygame.event == pygame.K_PAGEDOWN:
                delta = f'{int(delta) + 0.001}'
                ImagSur.set_image(image(lon, lat, delta))

        ImagSur.draw_image()
        ButtonOut.draw_button()

        pygame.display.flip()
        clock.tick(FPS)
