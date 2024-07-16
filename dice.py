import random
import pygame

class Dice(): # При инициации кубик либо принимает значение type или совершает бросок и получает случайное значение
    def __init__(self, type = None):
        self.type = type # Тип кубика

        self.image = None # Изображение стороны кубика
        self.surf = None # Отображаемая поверхность

        self.type_of_dice = ['attack', 'defence', 'moral'] # Возможные типы кубика

        if self.type == None:
            self.rolling_dice()
        else:
            self._choice(self.type)

    def rolling_dice(self):
        self.type = self.type_of_dice[random.randint(0, 2)]
        self._choice(self.type)

    def attack_roll(self):
        self.type = self.type_of_dice[0]
        self._choice(self.type)

    def defence_roll(self):
        self.type = self.type_of_dice[1]
        self._choice(self.type)

    def moral_roll(self):
        self.type = self.type_of_dice[2]
        self._choice(self.type)

    def _choice(self, type):
        match type:
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

    def draw(self, screen, x, y):
        self.rect = self.surf.get_rect(topleft=(x, y))
        screen.blit(self.surf, self.rect)