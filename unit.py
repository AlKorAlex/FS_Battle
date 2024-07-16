
import pygame
class Unit():
    def __init__(self, name, type, com_lvl, dice, health, moral, image):
        self.name = name
        self.type = type
        self.com_lvl = com_lvl
        self.health = health
        self.dice = dice
        self.moral = moral
        self.image = image

        self.demoralized = False

        self.surf_normal = pygame.image.load(self.image)  # создание поверхности из картинки юнита
        self.surf = pygame.transform.scale(self.surf_normal, (90, 90))

        self.green_line = False  # Отображение обводки при выборе

    def demoralization(self):
        """Деморализует отряд"""
        self.demoralized = True

    def moralization(self):
        """Восстанавливает отряд"""
        self.demoralized = False

    def damage_check(self, damage):
        if damage >= self.health:
            return True # юнит убит
        else:
            self.demoralization()
            return False # Юнит жив

    def info_from_battle(self, number):
        if self.demoralized == True:
            condition = 'Деморализован'
        else:
            condition = 'В порядке'
        print('Номер - ', number, 'Имя - ', self.name, ', Hp - ', self.health, ', Moral - ', self.moral, 'Состояние - ', condition)

    def draw_unit(self, screen, x, y,):

        self.rect = self.surf.get_rect(topleft=(x, y))
        if self.green_line == True:
            pygame.draw.rect(self.surf, (0, 255, 0), (0, 0, self.surf.get_width(), self.surf.get_height()), 5)
        screen.blit(self.surf, self.rect)
