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
    def __len__(self):
        if isinstance(self.number_of_floors, int):
            return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

penthouse = House("Пентхаус", 5)
penthouse.go_to(5)
penthouse.go_to(10)