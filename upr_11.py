grades = {
    "Ани": 6,
    "Боби": 5,
    "Мими": 4
}

while True:

    print(f"1 Добавяне на нов ученик")
    print(f"2. Промяна на оценка")
    print(f"3. Премахване на учник")
    print(f"4. Отпечатване на резултат")
    print(f"0. Изход")

    command = input("Направете избор: ")

    if command == "1":
        name = input("Име: ")
        mark = int(input("Оценка: "))
        grades[name] = mark

    elif command == "2":
        name = input("Име: ")
        if name in grades:
            grades[name] = int(input("Въведи оценка: "))
        else:
            print(f"Няма ученик с име {name}")
    elif command == "3":
        name = input("Име: ")
        if name in grades:
            del grades[name]
        else:
            print(f"Няма ученик с име {name}")
    elif command == "4":
        for k, v in grades.items():
            print(f"{k}: {v}")
    elif command == "0":
        break

