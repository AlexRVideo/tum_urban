class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self


    def __iadd__(self, value):
        return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)


h1 = House('ЖК Эльбрус', 30)
h1.go_to(8)

h2 = House('Дом на улице Твардовского', 4)
h2.go_to(7)

print(str(h1))
print(str(h2))

print(h1==h2) #eq
print(h1<h2) #__lt__
print(h1<=h2) #__le__
print(h1>h2) #__gt__
print(h1<=h2) #__ge__
print(h1!=h2) #__ne__

h1 = h1 + 8  # __add__
print(h1)


h2 += 10  # __iadd__
print(h1)
print(h1 == h2)

h2 = 24 + h2  # __radd__
print(h2)
print(h1 == h2)


print(h1<h2) #__lt__
print(h1<=h2) #__le__
print(h1>h2) #__gt__
print(h1<=h2) #__ge__
print(h1!=h2) #__ne__

