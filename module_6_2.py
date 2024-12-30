class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner: str, model: str, color: str, engin_power: int):
        self.owner = owner
        self.__model = model
        self.__color = color if self.is_color_valid(color) else 'unknown'
        self.__engin_power = engin_power

    def is_color_valid(self, color: str) -> bool:
        return color.lower() in {c.lower() for c in Vehicle.__COLOR_VARIANTS}

    def get_model(self) -> str:
        return f"Модель: {self.__model}"

    def get_horsepower(self) -> str:
        return f"Мощность двигателя: {self.__engin_power}"

    def get_color(self) -> str:
        return f"Цвет: {self.__color}"

    def print_info(self) -> None:
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color: str) -> None:
        if self.is_color_valid(new_color):
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner: str, model: str, color: str, engen_power: int):
        super().__init__(owner, model, color, engen_power)

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()