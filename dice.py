import random
import pygame

class Dice(): # При инициации кубик либо принимает значение type или совершает бросок и получает случайное значение
    def __init__(self, type = None):
        self.type = type # Тип кубика

        self.image = None # Изображение стороны кубика
        self.surf = None # Отображаемая поверхность

        self.type_of_dice = ['attack', 'defence', 'moral'] # Возможные типы кубика

        self.green_line = False  # Отображение обводки при выборе

        if self.type == None:
            self.rolling_dice()
        else:
            self._choice()

        self.rect = None



    def rolling_dice(self):
        self.type = self.type_of_dice[random.randint(0, 2)]
        self._choice()

    def attack_roll(self):
        self.type = self.type_of_dice[0]
        self._choice()

    def defence_roll(self):
        self.type = self.type_of_dice[1]
        self._choice()

    def moral_roll(self):
        self.type = self.type_of_dice[2]
        self._choice()

    def _choice(self):
        match self.type:
            case 'attack':
                self.image = 'images/Battle/Attack_Cube.jpg'
                self.surf = pygame.image.load(self.image)
                self.surf = pygame.transform.scale(self.surf, (60, 60))  # Уменьшить размер до 60
            case 'defence':
                self.image = 'images/Battle/Defence_Cube.jpg'
                self.surf = pygame.image.load(self.image)
                self.surf = pygame.transform.scale(self.surf, (60, 60))  # Уменьшить размер до 60
            case 'moral':
                self.image = 'images/Battle/Moral_Cube.jpg'
                self.surf = pygame.image.load(self.image)
                self.surf = pygame.transform.scale(self.surf, (60, 60))  # Уменьшить размер до 60

    def draw(self, screen, x, y, x_add=0, y_add=0):
        self._choice()
        self.rect = self.surf.get_rect(topleft=(x, y))
        if self.green_line == True:
            pygame.draw.rect(self.surf, (0, 255, 0), (0, 0, self.surf.get_width(), self.surf.get_height()), 5)
        screen.blit(self.surf, self.rect)
        self.rect = self.surf.get_rect(topleft=(x+x_add, y+y_add))