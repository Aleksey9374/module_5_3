'''Необходимо дополнить класс House специальными методами:
__eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и
возвращать результаты сравнения по соответствующим операторам. Как и в методе __eq__ в
сравнении участвует кол-во этажей.
__add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
__radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова). 
Для более точной логики работы методов __eq__, __add__ и других методов сравнения и арифметики перед выполняемыми действиями убеждаемся
в принадлежности к типу при помощи функции isinstance:
isinstance(other, int) - other указывает на объект типа int.
isinstance(other, House) - other указывает на объект типа House."'''

class House:
    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

# __eq__
    def __eq__(self, other):
        if isinstance(other.number_of_floors,int) and isinstance(other,House):
            return self.number_of_floors == other.number_of_floors
        else:
            return self
# __add__
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
           return self

# __radd__
    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
           return self

# __iadd__
    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
           return self
# __lt__
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
# __le__
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
# __gt__
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
# __ge__
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
# __ne__
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
