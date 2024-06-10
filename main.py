from game_stats import Game_stats
from player import Player
import pygame
from settings import Settings
from interface import Interface
from check_events import Check_Events


class FS:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создаёт игровые ресурсы"""

        # Создание экземпляра для хранения игровой статистики
        self.player_one = Player('Космодесантник', 8)
        self.player_two = Player('Орк', 8)
        self.game_stats = Game_stats(self.player_one, self.player_two)

        # Визуальная часть игры
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
        """Запуск основного цикла игры"""
        turn = True
        while True:
            self.game_stats.full_combat(self)  # Запуск полного цикла боя
            # Check_Events(self).check_events(None)
            self._update_screen()
            turn = False

    def _update_screen(self):
        self.interface.page('combat_interface')  # отрисовка страницы битвы
        pygame.display.update()
        self.clock.tick(self.FPS)







if __name__ == '__main__':
    # Создание экземпляра и запуск игры
    fs = FS()
    fs.run_game()