import pygame
from settings import Settings
from interface import Interface
class Main_Window:
    def __init__(self):
        """Инициализирует игру и создаёт игровые ресурсы"""

        # Визуальная часть игры
        pygame.init()  # Инициализирует настройки, необходимые Pygame для нормальной работы
        self.settings = Settings()

        # Настройка размера окна и его титульник
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Forbidden Stars - Combat")

        self.FPS = 30  # Частота обновления экрана
        self.clock = pygame.time.Clock()
        self.screen.fill(self.settings.bg_color)

    def main_f(self):
        pygame.display.update()
        self.clock.tick(self.FPS)
        return self.screen

