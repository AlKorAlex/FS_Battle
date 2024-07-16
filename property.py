from abc import ABC, abstractmethod
from interface import *
from check_events import Check_Events

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
        quest = Dice_Window(game_stats.screen, game_stats, player_number)
        quest.draw_window()
        pygame.display.update()
        choose_dice = game_stats._choose_dice(player_number, 2)
        for number in range(0, len(choose_dice)):
            choose_dice[number].defence_roll()



class Property_Base_Faith_Emperor(Property):
    def use_first_property(self, game_stats, player_number):
        print('Первое свойство: Получить 1 кубик')
        if game_stats.number_dice[player_number] < 8:
            game_stats._add_random_dice(player_number)
        else:
            print('Вы не можете получить кубик')

    def use_second_property(self, game_stats, player_number):
        print('Второе свойство: Либо восстановите 1 ваш отряд, либо получите кубик морали')
        # choose = int(input('1 - восстановить отряд, 2 - получить кубик морали, 0 - не использовать свойство'))
        # while choose != 1 or choose != 2 or choose != 0:
        #     if choose == 1:
        #         for i in range(0, len(player_number.army)): # Проверка на деморализованные отряды
        #             if player_number.army[i].demoralized == True:
        #                 continue
        #             else:
        #                 print('У вас нет деморализованных отрядов')
        #         army_demoralized = []
        #         for i in range(0, len(player_number.army)):
        #             if player_number.army[i].demoralized == True:
        #                 army_demoralized.append([i, player_number.army[i]])
        #
        #         # Выводим список деморализованных юнитов
        #         player_number._print_demoralized_unit_list(army_demoralized)
        #         choose_unit = int(input('Выберите юнит для восстановления(0 - отмена)\n'))
        #
        #         if choose_unit > 0 and choose_unit <= len(army_demoralized):
        #             player_number.army[army_demoralized[choose_unit - 1][0]].moralization()
        #         elif choose_unit == 0:
        #             break
        #         else:
        #             print('Неправильное значение, попробуйте ещё раз')
        #     elif choose == 2:
        #         player_number._add_dice('moral')



class Property_Base_Ambush(Property):
    def use_first_property(self, game_stats, player_number):
        # Получите 2 временные атаки
        game_stats.temporary_defence[player_number] += 2
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