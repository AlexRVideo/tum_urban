class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        obj.__init__(*args)
        cls.houses_history.append(obj.name)
        return obj

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')



h1 = House('ЖК Эльбрус', 30)
print(House.houses_history)
h2 = House('Дом на улице Твардовского', 4)
print(House.houses_history)
h3 = House('ЖК Пчелы', 16)
print(House.houses_history)

del h2
del h3

print(House.houses_history)

