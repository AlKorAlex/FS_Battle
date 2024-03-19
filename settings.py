
class Settings():
    "Класс для хранения всех настроек игры FS"

    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры игры
        # Игра запускается в неактивном состоянии
        self.game_active = False

        # Параметры экрана
        self.screen_width = 1920    # Ширина экрана
        self.screen_height = 1080   # Высота экрана
        self.bg_color = (230, 230, 230) # Цвет фона
        self.FPS = 60  # Частота обновления экрана

        # Цвета
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)

        # Тип кубиков
        self.type_dice = ['damage', 'defence', 'moral']


