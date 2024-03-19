from abc import ABC, abstractmethod

class Property(ABC):
    @abstractmethod
    def use_first_property(self, player, game_stats=None):
        pass
    @abstractmethod
    def use_second_property(self, player, game_stats=None):
        pass

class Property_Base_Blessed_Armor(Property):
    def use_first_property(self, player, game_stats=None):
        print('Первое свойство: Получить 2 временные защиты')
        player.temporary_defence += 2

    def use_second_property(self, player, game_stats=None):
        print('Переверните до 2х своих кубиков на защиту')
        player._print_dice_list()
        for i in range(0, 2):
            dice = -1
            while dice > len(player.all_dice) or dice < 0:
                dice = int(input('\nВыберите кубик который хотите перевернуть (1-8) - кубы, 0 - не переворачивать\n'))
                if dice > 0 and dice <= len(player.all_dice):
                    player.all_dice[dice - 1].defence_roll()
                    for j in range(0, len(player.all_dice)):
                        print(player.all_dice[j].type, end=', ')
                elif dice == 0:
                    break
                else:
                    print('Неправильное значение попробуйте ещё раз')

class Property_Base_Faith_Emperor(Property):
    def use_first_property(self, player, game_stats=None):
        print('Первое свойство: Получить 1 кубик')
        if len(player.all_dice) != 8:
            player._add_dice()
        else:
            print('Вы не можете получить кубик')

    def use_second_property(self, player, game_stats=None):
        print('Второе свойство: Либо восстановите 1 ваш отряд, либо получите кубик морали')
        choose = int(input('1 - восстановить отряд, 2 - получить кубик морали, 0 - не использовать свойство'))
        while choose != 1 or choose != 2 or choose != 0:
            if choose == 1:
                for i in range(0, len(player.army)): # Проверка на деморализованные отряды
                    if player.army[i].demoralized == True:
                        continue
                    else:
                        print('У вас нет деморализованных отрядов')
                army_demoralized = []
                for i in range(0, len(player.army)):
                    if player.army[i].demoralized == True:
                        army_demoralized.append([i, player.army[i]])

                # Выводим список деморализованных юнитов
                player._print_demoralized_unit_list(army_demoralized)
                choose_unit = int(input('Выберите юнит для восстановления(0 - отмена)\n'))

                if choose_unit > 0 and choose_unit <= len(army_demoralized):
                    player.army[army_demoralized[choose_unit-1][0]].moralization()
                elif choose_unit == 0:
                    break
                else:
                    print('Неправильное значение, попробуйте ещё раз')
            elif choose == 2:
                player._add_dice('moral')

class Property_Base_Ambush(Property):
    def use_first_property(self, player, game_stats=None):
        # Получите 2 временные атаки
        # player.temporary_attack += 2
        pass

    def use_second_property(self, player, game_stats=None):
        # Если в этом раунде боя отряд противника становится деморализованным,
        # то он уничтожается, если владелец не уплатит кубик морали
        pass

class Property_Base_Rage_Ultramar(Property):
    def use_first_property(self, player, game_stats=None):
        # Ваш противник должен перебросить 1 кубик защиты
        # Затем вы можете перебросить 1 кубик защиты
        pass
    def use_second_property(self, player, game_stats=None):
        # Космодесант/Ударный крейсер:
        # Противник должен потерять либо 1 кубик защиты, либо 2 временные защиты
        pass

class Property_Base_Scouts(Property):
    def use_first_property(self, player, game_stats=None):
        pass
    def use_second_property(self, player, game_stats=None):
        pass