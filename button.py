import pygame.font

class Button_any():
    """Создаёт кнопку с множеством настроек"""
    def __init__(self, screen, msg, width, height, x, y, button_color):
        """Инициализирует атрибуты кнопки"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Назначение размеров и свойств кнопок
        # self.width, self.height = 200, 50
        # (0, 255, 0)
        self.button_color = button_color
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Построение объекта rect кнопки и выравнивание по центру экрана
        self.rect = pygame.Rect(x, y, width, height)
        # self.rect.center = self.screen_rect.center

        # Сообщение кнопки создаётся только 1 раз
        self._preg_msg(msg)

    def _preg_msg(self, msg):
        """Преобразует msg в прямоугольник и выравнивает текст по центру"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        # Отображение пустой кнопки и вывод сообщения
        self.screen.fill(self.button_color, self.rect)
        # self.screen.blit(self.image, self.msg_image_rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)





