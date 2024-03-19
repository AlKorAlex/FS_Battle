
class Unit():
    def __init__(self, name, type, com_lvl, dice, health, moral):
        self.name = name
        self.type = type
        self.com_lvl = com_lvl
        self.health = health
        self.dice = dice
        self.moral = moral

        self.demoralized = False

    def demoralization(self):
        """Деморализует отряд"""
        self.demoralized = True

    def moralization(self):
        """Восстанавливает отряд"""
        self.demoralized = False

    def damage_check(self, damage):
        if damage >= self.health:
            return True
        else:
            return False

    def info_from_battle(self, number):
        if self.demoralized == True:
            condition = 'Деморализован'
        else:
            condition = 'В порядке'
        print('Номер - ', number, 'Имя - ', self.name, ', Hp - ', self.health, ', Moral - ', self.moral, 'Состояние - ', condition)

