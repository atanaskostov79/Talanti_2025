from datetime import datetime

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, year):
        current_year = datetime.now().year
        age = current_year - year
        return cls(name, age)

peter = Person.from_birth_year("Peter", 1925)
print(peter.name)
print(peter.age)

ivan = Person("Ivan", 34)
print(ivan.name)
print(ivan.age)