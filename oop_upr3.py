class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal makes a sound")

    def run(self):
        print("Animal runs")

class Dog(Animal):
    def speak(self):
        print("Woof!")
    def eat(self):
        print("Eating meat!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

dog = Dog("Dog")
cat = Cat("Cat")
dog.speak()
dog.eat()
dog.run()

cat.speak()
cat.run()

animal = Animal("Animal")
animal.speak()