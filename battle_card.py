from property import *
import pygame

class Battle_card():
    def __init__(self, name , price, com_lvl, attack, defence, moral, image, image_back, text_first, text_second, condition, property):
        self.name = name
        self.price = price
        self.com_lvl = com_lvl
        self.attack = attack
        self.defence = defence
        self.moral = moral
        self.image = image
        self.image_back = image_back
        self.text_first = text_first
        self.text_second = text_second
        self.condition = condition

        self.property = property # Способности карт

        self.surf_normal = pygame.image.load(self.image) # создание поверхности из картинки карты
        self.back = pygame.image.load(self.image_back)
        self.surf = pygame.transform.scale(self.surf_normal, (self.surf_normal.get_width() // 4.16, self.surf_normal.get_height() // 4.16))
        self.surf_back = pygame.transform.scale(self.back, (self.back.get_width() // 4.16, self.back.get_height() // 4.16))

        self.green_line = False # Отображение обводки при выборе

    def first_property_condition(self, game_stats, player_number):
        #Первое свойство карты
        self.property.use_first_property(self, game_stats, player_number)


    def second_property_condition(self, game_stats, player_number):
        """Проверка условия второго свойства карты"""
        # Проверка условий
        for j in range(0, len(self.condition)):
            for i in range(0, len(game_stats.army[player_number])):
                if game_stats.army[player_number][i].name == self.condition[j] \
                        and game_stats.army[player_number][i].demoralized == False:
                    text = 0
                    while text != 1 or text != 2:
                        text = int(input('Вы хотите использовать второе свойство карты? 1 - да, 2 - нет\n'))
                        if text == 1:
                            self.property.use_second_property(self, player_number, game_stats)
                            break
                        elif text == 2:
                            break
                        else:
                            print('Неправильное значение, повторите попытку')
        else:
            print('Вы не можете использовать второе свойство')


    def _info(self):
        print("Информация по карте: ", self.name)
        pass

    def draw_card(self, screen, x, y, turn):
        if turn == 'up':
            self.rect = self.surf.get_rect(topleft=(x, y))
            if self.green_line == True:
                pygame.draw.rect(self.surf, (0, 255, 0), (0, 0, self.surf.get_width(), self.surf.get_height()), 5)
            screen.blit(self.surf, self.rect)
        elif turn == 'back':
            self.rect = self.surf_back.get_rect(topleft=(x, y))
            screen.blit(self.surf_back, self.rect)





class all_cards_cosmo():
    def __init__(self):
        self.base_cards = [['Благословлённая броня', 0, 0, 0, 1, 0, None, 'Получите 2 временные защиты', 'Бастион/Космодесантник/Ударный крейсер: Переверните до 2х своих кубиков на защиту', ['Космодесантник'], Property_Base_Blessed_Armor],
                      ['Вера в Императора', 0, 0, 0, 0, 1, None, 'Получите 1 кубик', '', ['Космодесантник'], Property_Base_Faith_Emperor],
                      ['Засада', 0, 0, 1, 0, 0, None, None, None, ['Космодесантник'], Property_Base_Ambush],
                      ['Разведка', 0, 0, 0, 1, 0, None, ['Космодесантник'], '', '', Property_Base_Scouts],
                      ['Ярость Ультрамара', 0, 0, 1, 0, 0, None, ['Космодесантник'], '', '', Property_Base_Rage_Ultramar]]
        lvl_0_cards = [[], [], [], []]

