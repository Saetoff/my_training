import math

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = self.__initialize_sides(sides)
        self.__color = list(color)
        self.filled = False

    def __initialize_sides(self, sides):    # метод иниацилизирует стороны фигуры,
        if len(sides) == self.sides_count:
            return list(sides)
        else:
            return [1] * self.sides_count  # Заполняем единицами, если количество сторон некорректно

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and 0 <= r <= 255:
            if isinstance(g, int) and 0 <= g <= 255:
                if isinstance(b, int) and 0 <= b <= 255:
                    return True
        return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print("Invalid color values. The color remains unchanged.")

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *new_sides):
        return all(isinstance(side, (int, float)) and side > 0 for side in new_sides) and len(new_sides) == self.sides_count

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)  # Периметр для многоугольника


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference):
        super().__init__(color, circumference)  # Передаем длину окружности как сторону
        self.update_radius()  # Обновляем радиус при инициализации

    def update_radius(self):
        if self.get_sides():
            self.__radius = self.get_sides()[0] / (2 * math.pi)  # Вычисляем радиус по длине окружности
        else:
            self.__radius = 0  # Если __sides не инициализирован, устанавливаем радиус в 0

    def get_square(self):
        return math.pi * (self.__radius ** 2)

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        self.update_radius()  # Обновляем радиус после изменения стороны


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 1:
            self.__sides = [sides[0]] * self.sides_count  # 12 одинаковых сторон
        else:
            self.__sides = [1] * self.sides_count  # Заполняем единицами, если количество сторон некорректно

    def get_volume(self):
        return self.get_sides()[0] ** 3  # Объём куба



circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())  # [55, 66, 77]
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())  # [222, 35, 130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())  # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())  # [15]

# Проверка периметра (круга), это и есть длина:
print(len(circle1))  # 15

# Проверка объёма (куба):
print(cube1.get_volume())  # 216
