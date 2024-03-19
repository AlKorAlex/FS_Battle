import pygame
from interface import Interface
from settings import Settings

class Draw_Window():
    def __init__(self):
        pygame.init()  # Инициализирует настройки, необходимые Pygame для нормальной работы
        self.settings = Settings()

        # Настройка размера окна и его титульник
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Forbidden Stars - Combat")

        self.FPS = 60  # Частота обновления экрана
        self.clock = pygame.time.Clock()
        self.screen.fill(self.settings.bg_color)
        self.interface = Interface(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            self.interface.page('combat_interface')
            self.clock.tick(self.FPS)
            pygame.display.update()




# Создание экземпляра и запуск игры
fs = Draw_Window()
fs.run_game()