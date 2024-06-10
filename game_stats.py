from abc import ABC, abstractmethod
from property import *
from SpaceMarines import *
from check_events import Check_Events
from interface import Question_Window
from interface import Unit_Window
import pygame
class Game_stats():
    """Отслеживает статистику для игры FS"""

    def __init__(self, player_attacker, player_defender):
        """Инициализирует статистику"""
        self.player_attacker = player_attacker
        self.player_defender = player_defender
        self.players = [self.player_attacker, self.player_defender]
        self.players_cards = []
        self.active_stage = 0


    def full_combat(self, screen):
        if self.active_stage == 0:
            self.stage_prepare()
            self.active_stage = 1
        elif self.active_stage == 1:
            self.stage_combat(screen)
            self.active_stage = 2
        elif self.active_stage == 2:
            self.stage_final()
        # self.stage_prepare()
        # self.stage_combat(screen)
        # self.stage_final()


    def stage_prepare(self):
        # Бросок кубиков (Встроен в player)

        # Набор боевых карт
        self.player_attacker._form_base_deck()
        self.player_defender._form_base_deck()
        self.player_attacker.formation_battle_deck()
        self.player_defender.formation_battle_deck()

        # Вызов подкреплений (Не реализовано)


    def stage_combat(self, fs_game):
        for number_round in range(0, 3):
            self.round_combat(fs_game)

    def round_combat(self, fs_game):
        # Выбор боевых карт
        self._choose_combat_cards()

        # Розыгрыш боевых карт
        for i in range(0, 2):
            turn = True
            self.quest = Question_Window(fs_game.screen, 1)
            while turn == True:
                self.quest.draw_window()
                pygame.display.update()
                match Check_Events(self).check_events("question"):
                    case True:
                        print("yes")
                        turn = False
                    case False:
                        print("No")
                        turn = False
            self.players[i].play_battle_card(self.players_cards[i])
            fs_game._update_screen()
        self.players_cards = []

        """Реализовать окно с получением урона"""
        self._taking_damage(fs_game.screen)
        fs_game._update_screen()

        # Обнуляем временные атаки и защиты
        self.player_attacker.temporary_attack = 0
        self.player_attacker.temporary_defence = 0

        self.player_defender.temporary_attack = 0
        self.player_defender.temporary_defence = 0

        # Проверка победы
        if len(self.player_attacker.army) == 0:
            print("Победил защищающийся")
            return 0
        elif len(self.player_defender.army) == 0:
            print("Победил атакующий")
            return 0

    def stage_final(self):
        if self.player_attacker.all_moral > self.player_defender.all_moral:
            print("По морали победил атакующий")
        else:
            print("По морали победил защищающийся")


    def _taking_damage(self, screen):
        for i in range(0, 2):
            damage = self.players[i].all_attack - self.players[i-1**i].all_defence
            if damage <= 0:
                damage = 0
            else:
                # Выбор юнита
                while damage > 0:
                    turn = True
                    self.units_window = Unit_Window(screen, self.players[i])
                    unit_number = None
                    while turn == True:
                        self.units_window.draw_window()
                        pygame.display.update()
                        check = Check_Events(self).check_events("unit")
                        if check != None:
                            if check != -1 and check != -2:
                                unit_number = check
                                print('unit_number - ', unit_number)
                                # print('damage - ', damage)
                                #
                                # print('damage2 - ', damage)

                            elif check == -1 and unit_number != None:
                                damage = self.players[i].take_damage(damage, unit_number)
                                print("Нажата кнопка подтвердить")
                                turn = False
                            elif check == -2:
                                print("Нажата кнопка сброс")
                                unit_number = None


                print("Done")


    def _choose_combat_cards(self):
        for i in range(0, 2):
            turn = True
            while turn == True:
                bk = Check_Events(self).check_events("choose_bk")
                if bk != None:
                    card = False
                    for k in range(0, len(self.players[i].battle_cards)):
                        if self.players[i].battle_cards[k] == bk:
                            self.number = k
                            card = True
                            break
                    if card == True:
                        self.players_cards.append(self.number)
                        #print(self.players_cards)
                        turn = False
                    else:
                        print("Неправильная карта")



