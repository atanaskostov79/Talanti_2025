class Temperature:

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9

print(Temperature.celsius_to_fahrenheit(100))
print(Temperature.fahrenheit_to_celsius(100))