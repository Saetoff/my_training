class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor: int):
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

    def __lt__(self,other): # Меньше чем
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors < other

    def __gt__(self, other): # Больше чем
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors > other

    def __eq__(self, other): # Оператор равенства
        if isinstance(self.number_of_floors, int) and isinstance(other, object):
            return self.number_of_floors == other

    def __le__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors <= other

    def __ge__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors >= other

    def __ne__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors != other

    def __add__(self, value):
        if isinstance(self.number_of_floors, int) and isinstance(value, int):
            self.number_of_floors += value
            return self.number_of_floors

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __del__(self):
        print(f'{self.name} снесен, но он остается в истории')




if __name__ == '__maine__':
    penthouse = House("Пентхаус", 5)
    penthouse.go_to(5)
    penthouse.go_to(10)