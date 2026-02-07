box = []

while True:
    command = input()
    if command == "END":
        break

    parts = command.split()

    if parts[0] == "ADD":
        box.append(parts[1])
    elif parts[0] == "TAKE" and box:
        box.pop()

if box:
    print(", ".join(box))
else:
    print("Empty")
