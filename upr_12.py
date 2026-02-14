grades = {
    "Ани": 6,
    "Боби": 5,
    "Мими": 4
}

def add_student():
    name = input("Име: ")
    mark = int(input("Оценка: "))
    grades[name] = mark


def change_grade(name):
    if name in grades:
        grades[name] = int(input("Въведи оценка: "))
    else:
        print(f"Няма ученик с име {name}")


def dell_student(name):
    if name in grades:
        del grades[name]
    else:
        print(f"Няма ученик с име {name}")


def print_grades():
    for k, v in grades.items():
        print(f"{k}: {v}")

def print_menu():
    print(f"1 Добавяне на нов ученик")
    print(f"2. Промяна на оценка")
    print(f"3. Премахване на учник")
    print(f"4. Отпечатване на резултат")
    print(f"0. Изход")


while True:
    print_menu()

    command = input("Направете избор: ")

    if command == "1":
        add_student()

    elif command == "2":
        name = input("Име: ")
        change_grade(name)

    elif command == "3":
        name = input("Име: ")
        dell_student(name)

    elif command == "4":
        print_grades()

    elif command == "0":
        break

