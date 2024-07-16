from abc import ABC, abstractmethod

class Property(ABC):
    @abstractmethod
    def use_first_property(self, game_stats, player_number):
        pass
    @abstractmethod
    def use_second_property(self, game_stats, player_number):
        pass

class Property_Base_Blessed_Armor(Property):
    def use_first_property(self, game_stats, player_number):
        print('Первое свойство: Получить 2 временные защиты')
        game_stats.temporary_defence[player_number] += 2

    def use_second_property(self, game_stats, player_number):
        print('Переверните до 2х своих кубиков на защиту')
        for i in range(0, 2):
            dice = -1
            while dice > len(player_number.all_dice) or dice < 0:
                dice = int(input('\nВыберите кубик который хотите перевернуть (1-8) - кубы, 0 - не переворачивать\n'))
                if dice > 0 and dice <= len(player_number.all_dice):
                    player_number.all_dice[dice - 1].defence_roll()
                    for j in range(0, len(player_number.all_dice)):
                        print(player_number.all_dice[j].type, end=', ')
                elif dice == 0:
                    break
                else:
                    print('Неправильное значение попробуйте ещё раз')

class Property_Base_Faith_Emperor(Property):
    def use_first_property(self, game_stats, player_number):
        print('Первое свойство: Получить 1 кубик')
        if game_stats.number_dice[player_number] < 8:
            game_stats._add_random_dice(player_number)
        else:
            print('Вы не можете получить кубик')

    def use_second_property(self, game_stats, player_number):
        print('Второе свойство: Либо восстановите 1 ваш отряд, либо получите кубик морали')
        choose = int(input('1 - восстановить отряд, 2 - получить кубик морали, 0 - не использовать свойство'))
        while choose != 1 or choose != 2 or choose != 0:
            if choose == 1:
                for i in range(0, len(player_number.army)): # Проверка на деморализованные отряды
                    if player_number.army[i].demoralized == True:
                        continue
                    else:
                        print('У вас нет деморализованных отрядов')
                army_demoralized = []
                for i in range(0, len(player_number.army)):
                    if player_number.army[i].demoralized == True:
                        army_demoralized.append([i, player_number.army[i]])

                # Выводим список деморализованных юнитов
                player_number._print_demoralized_unit_list(army_demoralized)
                choose_unit = int(input('Выберите юнит для восстановления(0 - отмена)\n'))

                if choose_unit > 0 and choose_unit <= len(army_demoralized):
                    player_number.army[army_demoralized[choose_unit - 1][0]].moralization()
                elif choose_unit == 0:
                    break
                else:
                    print('Неправильное значение, попробуйте ещё раз')
            elif choose == 2:
                player_number._add_dice('moral')

class Property_Base_Ambush(Property):
    def use_first_property(self, game_stats, player_number):
        # Получите 2 временные атаки
        # player.temporary_attack += 2
        pass

    def use_second_property(self, game_stats, player_number):
        # Если в этом раунде боя отряд противника становится деморализованным,
        # то он уничтожается, если владелец не уплатит кубик морали
        pass

class Property_Base_Rage_Ultramar(Property):
    def use_first_property(self, game_stats, player_number):
        # Ваш противник должен перебросить 1 кубик защиты
        # Затем вы можете перебросить 1 кубик защиты
        pass
    def use_second_property(self, game_stats, player_number):
        # Космодесант/Ударный крейсер:
        # Противник должен потерять либо 1 кубик защиты, либо 2 временные защиты
        pass

class Property_Base_Scouts(Property):
    def use_first_property(self, game_stats, player_number):
        pass
    def use_second_property(self, game_stats, player_number):
        pass