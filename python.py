# __init__
# __str__

class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Пользователь {self.name}"


# class User:
#     pass
# user = User()
# print(user)


print("Hello world")

# __len__
# __add__

class Team:
    def __init__(self,members):
        self.members = members

    def __len__(self):
        return len(self.members)
    
team = Team("Алишер", "Нурсултан", "Бексултан")

print(len(team))


class Money:
    def __init__(self,amount):
        self.amount = amount #self

    def __add__(self, other):
        return Money(self.amount + other.amount)
    
    def __str__(self):
        return str(self.amount)

m1 = Money(100)
m2 = Money(50)

print(m1 + m2)

# 150
#cls 

#  Создайте класс Фруктов будет название фрукта, Откуда он,
#  И срок годности Выведиите так Фрукт: Название,
#  Срок: дата,
#  Изготовитель: Имя

# Вывод такой ---- сделайте вывод пары фруктов
# Фрукт: Название, Срок: дата,  Изготовитель: Имя

class Math:

    @staticmethod
    def add(a, b):
        return a + b 
    
print(Math.add(5, 3))

class Human:

    def normal(self):
        pass # Нет декоратора - Метод получает self

    @classmethod    
    def cls_method(cls):
        pass # @classmethod - Метод получает cls

    @staticmethod
    def static_method():
        pass # @staticmethod - Метод не получает self и cls

# Декоратор — это функция, которая изменяет поведение другой функции.

