class Vehicle:
    _COLOR_VARIANTS = ['red', 'yellow', 'blue', 'black', 'green', 'gray', 'white']

    def __init__(self, owner: str, __model: str, __engine_power: int, __color: str):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self, __model):
        return print(f'Модель: {self.__model}')

    def get_horsepower(self, __engine_power):
        return print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self, __color):
        return print(f'Цвет: {self.__color}')

    def print_info(self):
        print(self.get_model(self))
        print(self.get_horsepower(self))
        print(self.get_color(self))
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color: str):
        if new_color in self._COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

if __name__ == '__main__':
    # Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

    # Изначальные свойства
    vehicle1.print_info()

    # Меняем свойства (в т.ч. вызывая методы)
    vehicle1.set_color('Pink')
    vehicle1.set_color('BLACK')
    vehicle1.owner = 'Vasyok'

    # Проверяем что поменялось
    vehicle1.print_info()
