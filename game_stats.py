from abc import ABC, abstractmethod
from property import *
from SpaceMarines import *
from check_events import Check_Events
class Game_stats():
    """Отслеживает статистику для игры FS"""

    def __init__(self, player_attacker, player_defender):
        """Инициализирует статистику"""
        self.player_attacker = player_attacker
        self.player_defender = player_defender
        self.players = [self.player_attacker, self.player_defender]
        self.players_cards = []
        self.active_stage = 0


    def full_combat(self):
        if self.active_stage == 0:
            self.stage_prepare()
            self.active_stage = 1
        elif self.active_stage == 1:
            self.stage_combat()
        elif self.active_stage == 2:
            self.stage_final()
    def stage_prepare(self):
        # Бросок кубиков (Встроен в player)

        # Набор боевых карт
        self.player_attacker._form_base_deck()
        self.player_defender._form_base_deck()
        self.player_attacker.formation_battle_deck()
        self.player_defender.formation_battle_deck()

        # Вызов подкреплений (Не реализовано)


    def stage_combat(self):
            self.round_combat()

    def round_combat(self):
        # Выбор боевых карт
        self._choose_combat_cards()

        # Розыгрыш боевой карты
        for i in range(0, 2):
            self.players[i].play_battle_card(self.players_cards[i])
        self.players_cards = []

        self._taking_damage(self.player_attacker, self.player_defender)

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
        self.active_stage = 2

    def _taking_damage(self, player1, player2):
        # Шаг получения повреждений
        damage = player1.all_attack - player2.all_defence
        if damage < 0:
            damage = 0
        moral1 = player1.take_damage(damage)
        damage = player2.all_attack - player1.all_defence
        if damage < 0:
            damage = 0
        moral2 = player2.take_damage(damage)


    def stage_final(self):
        if self.player_attacker.all_moral > self.player_defender.all_moral:
            print("Победил защищающийся")
        else:
            print("Победил атакующий")
        self.active_stage = 3
        for i in range(0, 2):
            print(self.players[i].battle_cards)

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



