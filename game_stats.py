from abc import ABC, abstractmethod
from property import *
import random
from SpaceMarines import *
from check_events import Check_Events
from interface import Question_Window
from interface import Unit_Window
from dice import Dice
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

        """Рефакторинг"""
        self.number_dice = [0, 0] # +
        self.all_dice = [[], []] # +
        self.deck_cards = [[], []] # -
        self.hand_cards = [[], []] # +
        self.all_attack = [0, 0] # +
        self.all_defence = [0, 0] # +
        self.all_moral = [0, 0] # +
        self.using_battle_cards = [[], []] # -
        self.temporary_attack = [0, 0] # +
        self.temporary_defence = [0, 0] # +
        self.army = [[], []] # +


    def full_combat(self, fs_game):
        if self.active_stage == 0:
            self.stage_prepare()
            self.active_stage = 1
        elif self.active_stage == 1:
            self.stage_combat(fs_game)
            self.active_stage = 2
        elif self.active_stage == 2:
            self.stage_final()
        # self.stage_prepare()
        # self.stage_combat(fs_game)
        # self.stage_final()


    def stage_prepare(self):
        # Бросок кубиков
        self._form_random_unit_list()
        self._form_number_dice()
        self._rolling_dice()
        self._recalculation()
        self._form_base_deck()
        # Набор боевых карт

        # self.player_attacker.formation_battle_deck()
        # self.player_defender.formation_battle_deck()

        # Вызов подкреплений (Не реализовано)

    def play_battle_card(self, player, card):
        self.using_battle_cards[player].append(card)
        card.first_property_condition(self, player)
        card.second_property_condition(self, player)
        self.hand_cards[player].remove(card)
        self._recalculation()
        print(self.hand_cards[0])
        print(self.using_battle_cards)

    def stage_combat(self, fs_game):
        for number_round in range(0, 3):
            self.round_combat(fs_game)

    def round_combat(self, fs_game):
        # Выбор боевых карт
        self._choose_combat_cards(fs_game)
        # Розыгрыш боевых карт
        for i in range(0, 2): # Номер игрока
            fs_game._update_screen()
            turn = True #
            self.quest = Question_Window(fs_game.screen, 1)
            while turn == True:
                self.quest.draw_window()
                pygame.display.update()
                match Check_Events(self).check_events("question"):
                    case True:
                        # print("yes")
                        turn = False
                    case False:
                        # print("No")
                        turn = False
            self.play_battle_card(i, self.players_cards[i])
            fs_game._update_screen()
        self.players_cards = []

        """Распределение урона"""
        self._taking_damage(fs_game)
        fs_game._update_screen()

        # Обнуляем временные атаки и защиты
        self.player_attacker.temporary_attack = 0
        self.player_attacker.temporary_defence = 0

        self.player_defender.temporary_attack = 0
        self.player_defender.temporary_defence = 0

        # Проверка победы
        if len(self.army[0]) == 0:
            print("Победил защищающийся")
            return 0
        elif len(self.army[1]) == 0:
            print("Победил атакующий")
            return 0

    def stage_final(self):
        if self.all_moral[0] > self.all_moral[1]:
            print("По морали победил атакующий")
        else:
            print("По морали победил защищающийся")


    def _taking_damage(self, fs_game):
        for i in range(0, 2):
            fs_game._update_screen(i)
            self.screen = fs_game.screen
            damage = self.players[i].all_attack - self.players[i-1**i].all_defence
            if damage <= 0:
                damage = 0
            else:
                # Выбор юнита
                while damage > 0:
                    turn = True
                    self.units_window = Unit_Window(self.screen, self.players[i])
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


    def _choose_combat_cards(self, fs_game):
        for i in range(0, 2):
            fs_game._update_screen(i)
            turn = True
            while turn == True:
                bk = Check_Events(self).check_events("choose_bk")
                if bk != None:
                    card = False
                    for k in range(0, len(self.hand_cards[i])):
                        if self.hand_cards[i][k] == bk:
                            self.number = k
                            card = True
                            break
                    if card == True:
                        self.players_cards.append(bk)
                        turn = False
                    else:
                        print("Неправильная карта")


    def _form_random_unit_list(self):
        for j in range(0, 2):
            for i in range(0, 4):
                self.__add_unit(j, Space_Marines_Army().create_unit(random.randint(1, 6)))

    def __add_unit(self, player, troop):
        self.army[player].append(troop)

    def _form_number_dice(self):
        for i in range(0, 2):
            for j in range(0, len(self.army[i])):
                unit = self.army[i][j]
                self.number_dice[i] += unit.dice
                if self.number_dice[i] >= 8:
                    self.number_dice[i] = 8
                    break

    def _rolling_dice(self): #Бросок кубиков
        for i in range(0, 2):
            for number_dice in range(0, self.number_dice[i]):
                dice = Dice()
                dice.rolling_dice()
                self.all_dice[i].append(dice)


    def _recalculation(self):
        for j in range(0, 2):
            attack_dice = 0
            attack_temporary = self.temporary_attack[j]
            attack_card = 0

            defence_dice = 0
            defence_temporary = self.temporary_defence[j]
            defence_card = 0

            moral_dice = 0
            moral_card = 0
            moral_army = 0

            # Значения на кубах
            for i in range(0, self.number_dice[j]):
                match self.all_dice[j][i].type:
                    case 'attack':
                        attack_dice += 1
                    case 'defence':
                        defence_dice += 1
                    case 'moral':
                        moral_dice += 1

            # Значения на картах
            for i in range(0, len(self.using_battle_cards[j])):
                attack_card += self.using_battle_cards[j][i].attack
                defence_card += self.using_battle_cards[j][i].defence
                moral_card += self.using_battle_cards[j][i].moral

            # Мораль армии
            for i in range(0, len(self.army[j])):
                moral_army += self.army[j][i].moral

            self.all_attack[j] = attack_dice + attack_card + attack_temporary
            self.all_defence[j] = defence_dice + defence_card + defence_temporary
            self.all_moral[j] = moral_dice + moral_card + moral_army

    def _form_base_deck(self):
        for i in range(0, 2):
            self.hand_cards[i] = self.players[i].race._base_cards()

    def _add_random_dice(self, player_number):
        dice = Dice()
        self.number_dice += 1
        self.all_dice[player_number].append(dice)