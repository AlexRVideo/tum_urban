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

h1 = House('ЖК Эльбрус', 30)
h1.go_to(8)

h2 = House('Дом на улице Твардовского', 4)
h2.go_to(7)
