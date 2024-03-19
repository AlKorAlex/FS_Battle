from abc import ABC, abstractmethod

class BaseClass(ABC):
    @abstractmethod
    def function1(self):
        pass

class Class1(BaseClass):
    def function1(self):
        print("Original Function 1 in Class 1")

class Class2(BaseClass):
    def __init__(self, other_class):
        self.other_class = other_class

    def function1(self):
        print("Modified Function by Class 2")

    def change_function(self):
        # Вызываем измененную функцию
        self.other_class.function1 = self.function1
        self.other_class.function1()

class Class3(BaseClass):
    def __init__(self, other_class):
        self.other_class = other_class

    def function1(self):
        print("Modified Function by Class 3")

    def change_function(self):
        # Вызываем измененную функцию
        self.function1()

# Создаем экземпляры классов
obj1 = Class1()
obj2 = Class2(obj1)
obj3 = Class3(obj1)

# Используем исходную функцию
obj1.function1()  # Вывод: Original Function 1 in Class 1

# Изменяем функцию с использованием подклассов
obj2.change_function()  # Вывод: Modified Function by Class 2
obj3.change_function()  # Вывод: Modified Function by Class 3
