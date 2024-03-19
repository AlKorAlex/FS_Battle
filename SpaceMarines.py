from unit import Unit
from property import *
from battle_card import Battle_card

class Space_Marines_Army:
    def __init__(self):
        self.all_units = [['Разведчики', 'Troop', 0, 1, 2, 2, "images/Battle/Ultramarins_Units/0_Разведчики.png"],
                     ['Ударный крейсер', 'Ship', 0, 2, 2, 2, "images/Battle/Ultramarins_Units/0_Ударный крейсер.png"],
                     ['Космодесант', 'Troop', 1, 2, 3, 3, "images/Battle/Ultramarins_Units/1_Космодесант.png"],
                     ['Ленд Рейдер', 'Troop', 2, 3, 4, 4, "images/Battle/Ultramarins_Units/2_Боевая_Баржа.png"],
                     ['Боевая Баржа', 'Ship', 2, 4, 5, 4, "images/Battle/Ultramarins_Units/2_Ленд_Рейдер.png"],
                     ['Титан', 'Troop', 3, 3, 5, 4, "images/Battle/Ultramarins_Units/3_Титан.png"]]


    def create_unit(self, number):
        number -= 1
        n = []
        for i in range(0, 7):
            n.append(self.all_units[number][i])
        return Unit(n[0], n[1], n[2], n[3], n[4], n[5], n[6])

class Space_Marines_Cards:
    def __init__(self):
        self.all_cards = []
        self.lvl_base_cards = [['Благословлённая броня', 0, 0, 0, 1, 0, 'images/Battle/Ultramarins_combat_cards/Базовые карты/Base_Благословлённая_броня.png', 'Получите 2 временные защиты', 'Бастион/Космодесантник/Ударный крейсер: Переверните до 2х своих кубиков на защиту', ['Бастион', 'Космодесантник', 'Ударный крейсер'], Property_Base_Blessed_Armor],
                      ['Вера в Императора', 0, 0, 0, 0, 1, 'images/Battle/Ultramarins_combat_cards/Базовые карты/Base_Вера_в_Императора.png', 'Получите 1 кубик', 'Либо восстановите 1 ваш отряд, либо получите 1 кубик морали', ['Космодесантник'], Property_Base_Faith_Emperor],
                      ['Засада', 0, 0, 1, 0, 0, 'images/Battle/Ultramarins_combat_cards/Базовые карты/Base_Засада.png', 'Получите 2 временные атаки', 'Если в этом раунде боя отряд противника становится деморализованным, то он уничтожается, если владелец не уплатит 1 кубик морали', ['Космодесантник'], Property_Base_Ambush],
                      ['Разведка', 0, 0, 0, 1, 0, 'images/Battle/Ultramarins_combat_cards/Базовые карты/Base_Разведка.png', 'Если вы атакуете, то посмотрите закрытую карту боя противника. Получите либо 2 временные атаки, либо 2 временные защиты', 'Используйте 1 кубик морали для того, чтобы отступить из боя одним из свох отрядов', ['Космодесантник'], Property_Base_Scouts],
                      ['Ярость Ультрамара', 0, 0, 1, 0, 0, 'images/Battle/Ultramarins_combat_cards/Базовые карты/Base_Ярость_Ультрамара.png', 'Ваш противник должен перебросить 1 кубик защиты. Затем вы можете перебросить 1 кубик защиты', 'Противник должен потерять либо 1 кубик защиты, либо 2 временные защиты', ['Космодесантник', 'Ударный Крейсер'], Property_Base_Rage_Ultramar]]
        self.lvl_0_cards = [['Держать строй'],
                            ['Десантный модуль'],
                            ['Разведчики ветераны'],
                            ['Слава и Смерть']]
        self.lvl_2_cards = [['Бронекулак'],
                            ['Не ведать страха']]
        self.lvl_3_cards = [['Мощь Императора'],
                            ['Слава Императора']]

    def _number_deck(self, number_deck):
        deck = None
        match number_deck:
            case 0:
                deck = self.lvl_base_cards
            case 1:
                deck = self.lvl_0_cards
            case 2:
                deck = self.lvl_2_cards
            case 3:
                deck = self.lvl_3_cards
        return deck

    def create_card(self, number_deck, number_card):
        deck = self._number_deck(number_deck)
        o = []
        for i in range(0, 11):
            o.append(deck[number_card][i])
        return Battle_card(o[0], o[1], o[2], o[3], o[4], o[5], o[6], o[7], o[8], o[9], o[10])

    def _choose_card(self):
        deck = None
        for i in range(0,4):
            match i:
                case 0:
                    deck = self.lvl_base_cards
                case 1:
                    deck = self.lvl_0_cards
                case 2:
                    deck = self.lvl_2_cards
                case 3:
                    deck = self.lvl_3_cards
            print(i, ' - ', deck)
        number_deck = -1
        while number_deck < 0 and number_deck > 3:
            number_deck = int(input('Выберите колоду: \n'))-1
            match number_deck:
                case 0:
                    deck = self.lvl_base_cards
                case 1:
                    deck = self.lvl_0_cards
                case 2:
                    deck = self.lvl_2_cards
                case 3:
                    deck = self.lvl_3_cards
                case _:
                    print("Undefined")
        number_card = -1
        for i in range(0, len(deck)):
            print(i, ' - ', deck[i])
        while number_card < 0 and number_card > len(deck):
            number_card = int(input('Выберите карту: \n')) - 1
            if number_card < 0 or number_card > len(deck):
                print("Undefined")
        # return self.create_card(number_deck, number_card)
        return number_deck, number_card

    def _base_cards(self):
        card_list = []
        for i in range(0, 5):
            card_list.append(self.create_card(0, i))
        return card_list