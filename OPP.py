
class Car:

    car_color = ""
    # Конструктор
    def __init__(self, car_color):
        print("Start Class Car")
        self.car_color = car_color
    # Метод
    def print_color_1(self):
        print(self.car_color)
    # клас метод
    @classmethod
    def print_color(self):
        print(self.car_color)

    # Статичен метод
    @staticmethod
    def car_model():
        print(f"Car Model: BMW {Car.car_color}")

    @property
    def color(self):
        return self.car_color
    @color.setter
    def color(self, value):
        if len(value) == 0:
            self.car_color = "Red"
        else:
            self.car_color = value

if __name__ == '__main__':
    my_car = Car("Orange")
    my_car.color = ""
    my_car.print_color_1()
    # print(my_car.color)
    my_car.car_model()

