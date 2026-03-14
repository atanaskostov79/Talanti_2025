class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        print(f"Brand {self.brand}, Model {self.model}, Year {self.year}")


cars = [Car("Toyota", "Corola", 1999), Car("Ford", "Mustang", 2000)]

print(cars[1].year, cars[1].brand)

for car in cars:
    car.info()