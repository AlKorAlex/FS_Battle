class Class1:
    def function1(self):
        print("Original Function 1 in Class 1")

# Декораторы для изменения функции
def change_function_decorator1(func):
    def wrapper(*args, **kwargs):
        print("Modified Function by Decorator 1")
        return func(*args, **kwargs)
    return wrapper

def change_function_decorator2(func):
    def wrapper(*args, **kwargs):
        print("Modified Function by Decorator 2")
        return func(*args, **kwargs)
    return wrapper

# Класс, который применяет декораторы к функции другого класса
class Class2:
    def __init__(self, other_class):
        self.other_class = other_class

    def apply_decorators(self):
        self.other_class.function1 = change_function_decorator1(self.other_class.function1)
        self.other_class.function1 = change_function_decorator2(self.other_class.function1)

# Создаем экземпляры классов
obj1 = Class1()
obj2 = Class2(obj1)

# Используем исходную функцию
obj1.function1()  # Вывод: Original Function 1 in Class 1

# Применяем декораторы
obj2.apply_decorators()

# Проверяем изменение
obj1.function1()  # Вывод: Modified Function by Decorator 2, Modified Function by Decorator 1