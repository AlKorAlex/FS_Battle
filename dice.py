import random

class Dice():
    def __init__(self, type = None):
        self.type = None
        self.type_of_dice = ['attack', 'defence', 'moral']

        if type == None:
            self.rolling_dice()
        else:
            match type:
                case 'attack':
                    self.attack_roll()
                case 'defence':
                    self.defence_roll()
                case 'moral':
                    self.moral_roll()

    def rolling_dice(self):
        self.type = self.type_of_dice[random.randint(0, 2)]

    def attack_roll(self):
        self.type = self.type_of_dice[0]

    def defence_roll(self):
        self.type = self.type_of_dice[1]

    def moral_roll(self):
        self.type = self.type_of_dice[2]