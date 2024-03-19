from game_stats import Game_stats
from player import Player
import pygame
from settings import Settings
from interface import Interface
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
        # player = self.game_stats.player_attacker
        # self.game_stats.player_attacker._card_add(Battle_card('Благословлённая броня', 2, 0, 0, 1, 0, 'hui', 'agf', 'asf', ['Космодесантник'], Property_Base_Blessed_Armor))
        # self.game_stats.player_attacker._add_army(Unit('Космодесантник', 'Unit', 1, 3, 3, 3))
        # bk = self.game_stats.player_attacker.choose_battle_card()
        # self.game_stats.player_attacker.play_battle_card(bk)

        self.game_stats.full_combat() # Запуск полного цикла боя




        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    for j in range(0, 2): # Нажатие на карты в руке у обоих игроков
                        for i in range(0, len(self.game_stats.players[j].battle_cards)):
                            button_clicked = self.game_stats.players[j].battle_cards[i].rect.collidepoint(
                                mouse_pos)
                            if button_clicked:
                                print(self.game_stats.players[j].battle_cards[i].name)


            self.interface.page('combat_interface') # отрисовка страницы битвы
            self.clock.tick(self.FPS)
            pygame.display.update()





if __name__ == '__main__':
    # Создание экземпляра и запуск игры
    fs = FS()
    fs.run_game()