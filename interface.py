import pygame
from button import Button_any
from battle_card import Battle_card
from property import *
from game_stats import Game_stats
from settings import Settings

class Interface():
    """Отвечает за отрисовку всех страниц"""
    def __init__(self, fs_game):

        self.screen = fs_game.screen
        self.settings = fs_game.settings
        self.BLACK = (0, 0, 0)
        self.game_stats = fs_game.game_stats


    def page(self, page):
        self.screen.fill(self.settings.bg_color)
        match page:
            case 'main_menu':
                Main_Menu(self.screen).draw_main_menu()

            case 'combat_interface':
                self.combat_interface()

    def combat_interface(self):
        self._draw_lines() # Линии
        # c_card - созданная карта
        self.c_card = Battle_card('Благословлённая броня', 0, 0, 0, 1, 0, 'images/Battle/Ultramarins_combat_cards/0 Уровень/0_Держать_Строй.png', 'Получите 2 временные защиты', 'Бастион/Космодесантник/Ударный крейсер: Переверните до 2х своих кубиков на защиту', ['Бастион', 'Космодесантник', 'Ударный крейсер'], Property_Base_Blessed_Armor)

        # Отступы для карт
        w_s = (1.1 * self.settings.screen_width - 9.6 * self.c_card.surf.get_width()) // 12.8
        w_s2 = (1.1 * self.settings.screen_width - 6.4 * self.c_card.surf.get_width()) // 9.6

        for i in range(0, len(self.game_stats.player_attacker.battle_cards)): # Рисует карты на руке атакующего
            self.c_card = self.game_stats.player_attacker.battle_cards[i]
            if i < 3: # Рисует первые 3 карты на руке атакующего
                played_cards_position_x = (i + 1) * w_s + i * self.c_card.surf.get_width()
                played_cards_position_y = self.settings.screen_height // 3 + w_s * 2
                self.c_card.draw_card(self.screen, played_cards_position_x, played_cards_position_y)
            elif i >= 3: # Рисует нижние 2 карты на руке атакующего
                played_cards_position_x = (i + 1 - 3) * w_s2 + (i - 3) * self.c_card.surf.get_width()
                played_cards_position_y = self.settings.screen_height // 3 + w_s * 10
                self.c_card.draw_card(self.screen, played_cards_position_x, played_cards_position_y)

        for i in range(0, len(self.game_stats.player_attacker.using_battle_card)):  # Рисует сыгранные карты атакующего
            self.c_card = self.game_stats.player_attacker.using_battle_card[i]
            played_cards_position_x = (i + 1) * w_s + i * self.c_card.surf.get_width()
            played_cards_position_y = w_s * 2
            self.c_card.draw_card(self.screen, played_cards_position_x, played_cards_position_y)


        for i in range(0, len(self.game_stats.player_defender.battle_cards)):
            self.c_card = self.game_stats.player_defender.battle_cards[i]
            if i < 3:  # Рисует первые 3 карты на руке защищающегося
                played_cards_position_x = 2.1 * self.settings.screen_width // 3.2 + (
                        i + 1) * w_s + i * self.c_card.surf.get_width()
                played_cards_position_y = self.settings.screen_height // 3 + w_s * 2
                self.c_card.draw_card(self.screen, played_cards_position_x, played_cards_position_y)
            elif i >= 3:  # Рисует нижние 2 карты на руке защищающегося
                played_cards_position_x = 2.1 * self.settings.screen_width // 3.2 + (
                        i + 1 - 3) * w_s2 + (i - 3) * self.c_card.surf.get_width()
                played_cards_position_y = self.settings.screen_height // 3 + w_s * 10
                self.c_card.draw_card(self.screen, played_cards_position_x, played_cards_position_y)

        for i in range(0, len(self.game_stats.player_defender.using_battle_card)):  # Рисует сыгранные карты защищающегося
            self.c_card = self.game_stats.player_defender.using_battle_card[i]
            played_cards_position_x = 2.1 * self.settings.screen_width // 3.2 + (
                        i + 1) * w_s + i * self.c_card.surf.get_width()
            played_cards_position_y = self.settings.screen_height // 15
            self.c_card.draw_card(self.screen, played_cards_position_x, played_cards_position_y)




        for j in range(0, 2): # Отрисовывает кубики игроков
            for i in range(0, len(self.game_stats.players[j].all_dice)):  # Отрисовывает кубики нападающего
                match self.game_stats.players[j].all_dice[i].type:
                    case 'attack':
                        self.image = 'images/Battle/Attack_Cube.jpg'
                    case 'defence':
                        self.image = 'images/Battle/Defence_Cube.jpg'
                    case 'moral':
                        self.image = 'images/Battle/Moral_Cube.jpg'
                self.surf = pygame.image.load(self.image)
                self.surf = pygame.transform.scale(self.surf, (60, 60)) # Меняет размер картинки до 60x60

                x = self.settings.screen_width * 1.1 // 3.2 * abs(j-1) + j * self.screen.get_rect().midtop[0] # Начальное положение (Стенка)
                w_s = (self.settings.screen_width // 6.4 - 4 * self.surf.get_width()) // 5
                if i > 3:
                    played_cards_position_x = x + w_s * (i - 3) + self.surf.get_width() * (i - 4)
                    played_cards_position_y = 2 * w_s + self.surf.get_height()
                    self.rect = self.surf.get_rect(topleft=(played_cards_position_x, played_cards_position_y))
                    self.screen.blit(self.surf, self.rect)
                else:
                    played_cards_position_x = x + w_s * (i + 1) + self.surf.get_width() * i
                    played_cards_position_y = w_s
                    self.rect = self.surf.get_rect(topleft=(played_cards_position_x, played_cards_position_y))
                    self.screen.blit(self.surf, self.rect)


        for j in range(0, 2):
            k = 0
            for i in range(0, len(self.game_stats.players[j].army)):
                unit = self.game_stats.players[j].army[i] # Конкретный юнит

                x = self.settings.screen_width * 1.1 // 3.2 * abs(j - 1) + j * self.screen.get_rect().midtop[0]
                w_s = ((self.settings.screen_width // 6.4 - 2 * unit.surf.get_width()) // 2) # Переделать


                played_unit_position_x = x + w_s * (k + 1) + self.surf.get_width() * k
                if k == 0:
                    k = 1
                else:
                    k = 0
                played_unit_position_y = self.settings.screen_height // 3 + w_s * int(i/2) + int(i/2) * self.surf.get_height() + w_s
                unit.draw_unit(self.screen, played_unit_position_x, played_unit_position_y)



    def _draw_lines(self):
        color = self.settings.BLACK
        pygame.draw.line(self.screen, color, (self.screen.get_rect().midtop[0], 0),(self.screen.get_rect().midtop[0], self.screen.get_rect().midbottom[1]))
        pygame.draw.line(self.screen, color, (0, self.settings.screen_height // 3),(self.settings.screen_width, self.settings.screen_height // 3))
        pygame.draw.line(self.screen, color, (self.settings.screen_width * 1.1 // 3.2, 0), (self.settings.screen_width * 1.1 // 3.2, self.settings.screen_height))
        pygame.draw.line(self.screen, color,(self.settings.screen_width * 2.1 // 3.2, 0), (self.settings.screen_width * 2.1 // 3.2,self.settings.screen_height))

class Main_Menu():
    """Класс для отрисовки главного меню"""

    def __init__(self, screen):
        self.screen = screen

    def buttons_main_menu(self, name_button):
        match name_button:
            case 'Начать бой':
                return Button_any(self.screen, 'Начать бой', 200, 100, 0, 0, (0, 255, 0))
            case 'Настроить бой':
                return Button_any(self.screen, 'Настроить бой', 200, 100, 0, 150, (0, 255, 0))
            case 'Выход':
                return Button_any(self.screen, 'Выход', 200, 100, 0, 300, (0, 255, 0))

    def draw_main_menu(self):
        Button_any(self.screen, 'Начать бой', 200, 100, 0, 0, (0, 255, 0)).draw_button()
        Button_any(self.screen, 'Настроить бой', 200, 100, 0, 150, (0, 255, 0)).draw_button()
        Button_any(self.screen, 'Выход', 200, 100, 0, 300, (0, 255, 0)).draw_button()

class Question_Window():
    def __init__(self, fs_game):
        self.screen = fs_game.screen
        self.text = None
        self.surf = pygame.Surface((500, 500))
        self.surf.fill(Settings().RED)
        f = pygame.font.SysFont(None, 48)
        self.sc_text = f.render('Привет Мир!', 1, Settings().RED, Settings().BLACK)
        self.pos = self.sc_text.get_rect(center=(500//2, 500//2))
    def draw_question_window(self):
        self.surf.blit(self.sc_text, self.pos)
        Button_any(self.surf, 'Да', 200, 100, 50, 300, (0, 255, 0)).draw_button()
        Button_any(self.surf, 'Нет', 200, 100, 300, 300, (0, 255, 0)).draw_button()
        self.screen.blit(self.surf, (500, 500))