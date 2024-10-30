class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor: int):
        self.new_floor = new_floor
        if new_floor > self.number_of_floors or new_floor <1:
            print(f'Такого этажа не существует {new_floor}')
        else:
            for i in range(1, new_floor + 1):
                print(i)


penthouse = House("Пентхаус", 5)
penthouse.go_to(5)
penthouse.go_to(10)