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
zoom = 0.002
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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_PAGEUP:
                print("up")
                zoom += 0.0005
                ImagSur = Image(screen, image("37.530887", "55.703118", f"{zoom}"), (0, 0), (screen.get_width(), screen.get_height()))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_PAGEDOWN:
                print("down")
                zoom -= 0.0005
                if zoom < 0.001:
                    zoom = 0.001
                ImagSur = Image(screen, image("37.530887", "55.703118", f"{zoom}"), (0, 0), (screen.get_width(), screen.get_height()))

        ImagSur.draw_image()
        ButtonOut.draw_button()

        pygame.display.flip()
        clock.tick(FPS)
