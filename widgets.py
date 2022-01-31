import os
import pygame
from settings import *


class Button:
    def __init__(self, screen, text, pos, size, color_circuil, color_text, border=0, border_radius=16):  # Все нужное
        self.screen = screen  # Где рисуем
        self.pos_x, self.pos_y = pos  # Где именно рисуем
        self.width, self.height = size  # Размер
        self.color_circuil = color_circuil  # Цвет кнопки или контура
        self.color_text = color_text  # Цвет кнопки
        self.border = border  # Контур или заливка и размер
        self.border_radius = border_radius
        self.text = text
        self.font = pygame.font.Font(None, self.height)  # Нужный размер
        self.text_surf = self.font.render(self.text, True, self.color_text)  # Поверхность
        self.button = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)  # Сама кнопка

    def set_text(self, text):  # Можно изминить текст на кнопке
        self.text = text

    def set_size(self, pos, size):
        self.pos_x, self.pos_y = pos
        self.width, self.height = size
        self.font = pygame.font.Font(None, self.height)
        self.button = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)

    def set_color(self, color_circuil, color_text):
        self.color_circuil = color_circuil
        self.color_text = color_text

    def set_border(self, border, border_radius):
        self.border = border
        self.border_radius = border_radius

    def draw_button(self):  # Нарисовать кнопку и текст на ней
        self.text_surf = self.font.render(self.text, True, self.color_text)
        pygame.draw.rect(self.screen, self.color_circuil, self.button, self.border, self.border_radius)
        self.screen.blit(self.text_surf,
                         (self.pos_x + (self.width // 2 - self.text_surf.get_width() // 2),
                          self.pos_y + self.height // 5))

    def get_button(self):  # Это для проверки совмещения с мышью
        return self.button


class Image:
    def __init__(self, screen, name, pos, size=False, colorkey=False):  # Все нужное
        self.screen = screen  # Где рисуем
        self.pos_x, self.pos_y = pos  # Где именно рисуем
        self.image = pygame.Surface([100, 100])  # Создаем поверхность
        self.image.fill((0, 0, 0))  # Заливаем черным
        self.fullname = os.path.join('data', name)  # Находим путь к нужной картинке
        self.image = pygame.image.load(self.fullname)
        if colorkey:  # прозрачность
            self.image = self.image.convert()
            self.image.set_colorkey(self.image.get_at((0, 0)))  # убираем фон
        else:  # Не знаю че это, я просто скопировал из учебника
            self.image = self.image.convert_alpha()
        if size:  # Меняем размер если нужно
            self.width, self.height = size
            self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def set_image(self, name):  # Можно поменять картинку(недоделано)
        pass

    def draw_image(self):  # Рисуем
        self.screen.blit(self.image, (self.pos_x, self.pos_y))


class InputBox:
    def __init__(self, screen, pos, size=(140, 32), text=''):
        self.len = 0
        self.screen = screen
        self.x, self.y = pos
        self.w, self.h = size
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.font = pygame.font.Font(None, self.h)
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                    self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif self.font.size(self.text[:-1] + event.unicode)[0] < self.w - 20:
                    self.text += event.unicode
                self.txt_surface = self.font.render(self.text, True, self.color)
        self.draw()

    def draw(self):
        self.screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(self.screen, self.color, self.rect, 2)

    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text
