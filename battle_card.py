from property import *
import pygame

class Battle_card():
    def __init__(self, name , price, com_lvl, attack, defence, moral, image, text_first, text_second, condition, property):
        self.name = name
        self.price = price
        self.com_lvl = com_lvl
        self.attack = attack
        self.defence = defence
        self.moral = moral
        self.image = image
        self.text_first = text_first
        self.text_second = text_second
        self.condition = condition

        self.property = property # Способности карт

        self.surf_normal = pygame.image.load(self.image) # Нужно для отрисовки
        self.surf = pygame.transform.scale(self.surf_normal, (self.surf_normal.get_width() // 4.16, self.surf_normal.get_height() // 4.16))

    def first_property_condition(self, player):
        print(self.text_first)
        text = int(input('Вы хотите использовать первое свойство карты? 1 - да, 2 - нет\n'))
        if text == 1:
            self.property.use_first_property(self, player)


    def second_property_condition(self, player):
        """Проверка условия второго свойства карты"""
        print(self.text_second)
        cond = False
        # Проверка условий
        for j in range(0, len(self.condition)):
            for i in range(0, len(player.army)):
                if player.army[i].name == self.condition[j] and player.army[i].demoralized == False:
                    cond = True
                    continue
        if cond == True:
            text = 0
            while text != 1 or text != 2:
                text = int(input('Вы хотите использовать второе свойство карты? 1 - да, 2 - нет\n'))
                if text == 1:
                    self.property.use_second_property(player)
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

    def draw_card(self, screen, x, y,):
        self.rect = self.surf.get_rect(topleft=(x, y))
        screen.blit(self.surf, self.rect)





class all_cards_cosmo():
    def __init__(self):
        self.base_cards = [['Благословлённая броня', 0, 0, 0, 1, 0, None, 'Получите 2 временные защиты', 'Бастион/Космодесантник/Ударный крейсер: Переверните до 2х своих кубиков на защиту', ['Космодесантник'], Property_Base_Blessed_Armor],
                      ['Вера в Императора', 0, 0, 0, 0, 1, None, 'Получите 1 кубик', '', ['Космодесантник'], Property_Base_Faith_Emperor],
                      ['Засада', 0, 0, 1, 0, 0, None, None, None, ['Космодесантник'], Property_Base_Ambush],
                      ['Разведка', 0, 0, 0, 1, 0, None, ['Космодесантник'], '', '', Property_Base_Scouts],
                      ['Ярость Ультрамара', 0, 0, 1, 0, 0, None, ['Космодесантник'], '', '', Property_Base_Rage_Ultramar]]
        lvl_0_cards = [[], [], [], []]

