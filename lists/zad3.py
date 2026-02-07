inventory = []

while True:
    command = input("Enter command: ")
    if command == "END":
        break

    parts = command.split()
    action = parts[0]
    item = parts[1]

    if action == "ADD":
        if item not in inventory:
            inventory.append(item)

    elif action == "REMOVE":
        if item in inventory:
            inventory.remove(item)

    elif action == "CHECK":
        if item in inventory:
            print("Yes")
        else:
            print("No")

if inventory:
    print(", ".join(inventory))
else:
    print("Empty inventory")
