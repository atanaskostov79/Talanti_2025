queue = []

while True:
    command = input()
    if command == "END":
        break

    parts = command.split()

    if parts[0] == "JOIN":
        queue.append(parts[1])
    elif parts[0] == "SLIDE" and queue:
        queue.pop(0)

if queue:
    print(", ".join(queue))
else:
    print("No children")
