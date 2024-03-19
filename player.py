import random
from battle_card import Battle_card
from battle_card import all_cards_cosmo
from dice import Dice
from SpaceMarines import Space_Marines_Cards, Space_Marines_Army
class Player():
    def __init__(self, name, number_dice, race=None):

        self.name = name
        self.number_dice = number_dice
        self.all_dice = []
        self.all_card = []
        self.battle_cards = []
        self.all_attack = 0
        self.all_defence = 0
        self.all_moral = 0
        self.using_battle_card = []
        self.temporary_attack = 0
        self.temporary_defence = 0
        self.army = []
        self.race = Space_Marines_Cards()

        self._form_random_unit_list()
        self.first_rolling_dice()
        self._recalculation()

    def first_rolling_dice(self):
        """Первый бросок кубиков"""
        for number_dice in range(0, self.number_dice):
            dice = Dice()
            dice.rolling_dice()
            self.all_dice.append(dice)

    def _card_add(self, battle_card):
        # Добавить боевую карту в колоду
        self.all_card.append(battle_card)

    def _card_remove(self, battle_card):
        # Удалить боевую карту из колоды
        pass

    def choose_battle_card(self):
        # Выбрать боевую карту (Переделать)
        for i in range(0, len(self.battle_cards)):
            print(i + 1, ' ', self.battle_cards[i].name)
        bk = int(input('Выберите карту(номер): ')) - 1
        return bk

    def play_battle_card(self, number_battle_card):
        # Розыгрыш боевой карты
        card = self.battle_cards[number_battle_card] # Сама боевая карта
        self.using_battle_card.append(card) # Добавление боевой карты в использованные карты
        card.first_property_condition(self) # Первое свойство карты
        card.second_property_condition(self) # Второе свойство карты
        del self.battle_cards[number_battle_card]
        self._recalculation()

    def add_unit(self, troop):
        # Добавить юнита в армию
        self.army.append(troop)

    def create_unit(self):
        print('Выберите юнит, который хотите добавить:')
        for i in range(0, 6):
            pass

    def formation_battle_deck(self):
        # Сформировать боевую колоду (5 карт)
        all_card = self.all_card[:]
        for i in range(0, 5):
            card_number = random.randint(0, len(all_card))-1
            self.battle_cards.append(all_card[card_number])
            del all_card[card_number]

    def take_damage(self, damage):
        # Получение урона армией игрока
        while (damage != 0):
            print('Входящий урон: ', damage)
            print('Выберите юнита для получения урона')
            self._print_unit_list()
            unit = int(input('Введит номер юнита\n'))
            if self.army[unit-1].damage_check(damage) == True:
                damage -= self.army[unit-1].health
                del self.army[unit-1]
                return False
            else:
                damage = 0
                self.army[unit-1].demoralization()
                return True

    def _add_dice(self, type_dice = None):
        # Добавить кубик игроку
        dice = Dice(type_dice)
        self.all_dice.append(dice)


    def _recalculation(self):
        attack_dice = 0
        attack_temporary = self.temporary_attack
        attack_card = 0

        defence_dice = 0
        defence_temporary = self.temporary_defence
        defence_card = 0

        moral_dice = 0
        moral_card = 0
        moral_army = 0

        # Значения на кубах
        for i in range(0, self.number_dice):
            match self.all_dice[i].type:
                case 'attack':
                    attack_dice += 1
                case 'defence':
                    defence_dice += 1
                case 'moral':
                    moral_dice += 1

        # Значения на картах
        for i in range(0, len(self.using_battle_card)):
            attack_card += self.using_battle_card[i].attack
            defence_card += self.using_battle_card[i].defence
            moral_card += self.using_battle_card[i].moral

        # Мораль армии
        for i in range(0, len(self.army)):
            moral_army += self.army[i].moral

        self.all_attack = attack_dice + attack_card + attack_temporary
        self.all_defence = defence_dice + defence_card + defence_temporary
        self.all_moral = moral_dice + moral_card + moral_army

    def _info(self):
        print(self.name)
        print(self.number_dice)
        print(self.all_dice)
        print(self.battle_cards)
        print(self.all_attack)
        print(self.all_defence)
        print(self.all_moral)
        print(self.using_battle_card)
        print(self.temporary_attack)
        print(self.temporary_defence)
        print(self.army)

    def _print_unit_list(self):
        # Напечатать таблицу с армией игрока
        print('Армия:')
        for i in range(0, len(self.army)):
            unit = self.army[i]
            unit.info_from_battle(i + 1)

    def _print_demoralized_unit_list(self, unit_list):
        print('Деморализованные юниты')
        for i in range(0, len(unit_list)):
            unit = unit_list[i][1]
            unit.info_from_battle(i+1)
    def _print_dice_list(self):
        print('Кубики:')
        for j in range(0, len(self.all_dice)):
            print(self.all_dice[j].type, end=', ')

    def _form_base_deck(self):
        self.all_card = self.race._base_cards()

    def _form_custom_deck(self):
        pass

    def _form_random_unit_list(self):
        for i in range(0, 4):
            self.add_unit(Space_Marines_Army().create_unit(random.randint(1, 6)))
