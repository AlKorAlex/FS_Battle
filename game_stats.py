from abc import ABC, abstractmethod
from property import *
import random
from SpaceMarines import *
from check_events import Check_Events
from interface import Question_Window
from interface import Unit_Window
from interface import *
from dice import Dice
import pygame
class Game_stats():
    """Отслеживает статистику для игры FS"""

    def __init__(self, player_attacker, player_defender, screen):
        """Инициализирует статистику"""
        self.player_attacker = player_attacker
        self.player_defender = player_defender
        self.players = [self.player_attacker, self.player_defender]
        self.players_cards = []
        self.active_stage = 0
        self.screen = screen



        """Рефакторинг"""
        self.number_dice = [0, 0] # +
        self.all_dice = [[], []] # Кубики игроков
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
        for player in range(0, 2): # Номер игрока
            self.using_battle_cards[player].append(self.players_cards[player])
            for prop in range(0, 2): # Номер свойства карты

                # self.play_battle_card(player, self.players_cards[player])
                if prop == 0:
                    fs_game._update_screen()
                    turn = True
                    self.quest = Question_Window(self, player, prop)
                    while turn == True:
                        self.quest.draw_window()
                        pygame.display.update()
                        match Check_Events(self).check_events("question"):
                            case True:
                                # print("yes")
                                self.players_cards[player].first_property_condition(self, player)
                                turn = False
                            case False:
                                # print("No")
                                turn = False
                else:
                    for j in range(0, len(self.players_cards[player].condition)):
                        for i in range(0, len(self.army[player])):
                            if self.army[player][i].name == self.players_cards[player].condition[j] \
                                    and self.army[player][i].demoralized == False:
                                fs_game._update_screen()
                                turn = True
                                self.quest = Question_Window(self, player, prop)
                                while turn == True:
                                    self.quest.draw_window()
                                    pygame.display.update()
                                    match Check_Events(self).check_events("question"):
                                        case True:
                                            # print("yes")
                                            self.players_cards[player].second_property_condition(self, player)
                                            turn = False
                                        case False:
                                            # print("No")
                                            turn = False
            self.hand_cards[player].remove(self.players_cards[player])
            self._recalculation()


        fs_game._update_screen()
        self.players_cards = []

        """Распределение урона"""
        print(self.all_attack)
        print(self.all_defence)
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
        print(1)
        for i in range(0, 2):
            fs_game._update_screen(i)
            self.screen = fs_game.screen
            damage = self.all_attack[i] - self.all_defence[i-1**i]
            if damage <= 0:
                damage = 0
            else:
                # Выбор юнита
                while damage > 0:
                    turn = True
                    self.units_window = Unit_Window(self.screen, self, i)
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
                                if self.army[i][unit_number].damage_check(damage) == True:
                                    damage -= self.army[i][unit_number].health
                                    del self.army[unit_number]  # Удалить убитого юнита
                                    print("one")
                                else:
                                    damage = 0
                                    self.army[i][unit_number].demoralization()
                                    print("two")
                                print("Нажата кнопка подтвердить")
                                turn = False
                            elif check == -2:
                                print("Нажата кнопка сброс")
                                unit_number = None


                print("Done")


    def _choose_combat_cards(self, fs_game):
        '''Выбор карты для розыгрыша'''
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

    def _choose_dice(self, player_number, number_of_dice):
        '''Окно с выбором кубика'''
        self.dice_window = Dice_Window(self.screen, self, player_number)
        self.dice_window.draw_window()
        pygame.display.update()
        choose_dice = []
        turn = True
        while turn == True:
            check = Check_Events(self).check_events("dice")
            if check != None:
                if check != -1 and check != -2 and len(choose_dice) < number_of_dice:
                    # self.all_dice[player_number][check].green_line = True
                    choose_dice.append(self.all_dice[player_number][check])
                    for i in range(0, len(choose_dice)):
                        choose_dice[i].green_line = True

                elif check == -1:
                    print("Нажата кнопка подтвердить")
                    turn = False
                elif check == -2:
                    print("Нажата кнопка сброс")
                    # for i in range(0, len(self.all_dice[player_number])):
                    #     self.all_dice[player_number][i].green_line = False
                    for i in range(0, len(choose_dice)):
                        choose_dice[i].green_line = False
                    choose_dice = []
                self.dice_window.draw_window()
                pygame.display.update()

        for i in range(0, len(self.all_dice[player_number])):
            self.all_dice[player_number][i].green_line = False
        return choose_dice

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