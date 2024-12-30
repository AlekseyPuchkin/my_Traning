class Figure:
    def __init__(self, color):
        self.sides_count = 0
        self._sides = []
        self._color = color
        self.filled = False

    def get_color(self):
        return self._color

    def __is_valid_color(self, r, g, b):
        return isinstance(r, int) and isinstance(g, int) and isinstance(b, int) and \
               0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self._color = (r, g, b)

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            return False
        return all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        return self._sides

    def __len__(self):
        return sum(self._sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self._sides = list(new_sides)

class Circle(Figure):
    def __init__(self, color, *sides):
        super().__init__(color)
        self.sides_count = 1
        if len(sides) != self.sides_count:
            self.set_sides(1)
        else:
            self.set_sides(*sides)
        self.__radius = self._sides[0] / (2 * 3.14)

    def get_square(self):
        return 3.14 * self.__radius ** 2

class Triangle(Figure):
    def __init__(self, color, *sides):
        super().__init__(color)
        self.sides_count = 3
        if len(sides) != self.sides_count:
            self.set_sides(1, 1, 1)
        else:
            self.set_sides(*sides)

    def get_square(self):
        s = sum(self._sides) / 2
        return (s * (s - self._sides[0]) * (s - self._sides[1]) * (s - self._sides[2])) ** 0.5

class Cube(Figure):
    def __init__(self, color, side_length, *sides):
        super().__init__(color)
        self.sides_count = 12
        if len(sides) != self.sides_count:
            self.set_sides(*(side_length,) * self.sides_count)
        else:
            self.set_sides(*sides)

    def get_volume(self):
        return self._sides[0] ** 3

circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())

cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())

circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))
print(cube1.get_volume())