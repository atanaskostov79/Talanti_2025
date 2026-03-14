class Employee:

    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

        Employee.employee_count += 1

        if Employee.employee_count > 2:
            raise Exception("Too many employees")

    @classmethod
    def get_employee_cont(cls):
        return cls.employee_count

e1 = Employee("Ivan", 3400)
e2 = Employee("Peter", 2222)
e3 = Employee("Maria", 2000)

print(Employee.get_employee_cont())

