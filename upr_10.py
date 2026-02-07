
d = { "Matematika": 3 }
def averageGrade(d):
    sum = 0
    for v in d.values():
        sum += v
    print(d, sum / len(d))

while True:
    command = input()
    if command == "exit":
        break

    c, v = command.split()
    if c not in d:
        d[c] = int(v)

    averageGrade(d)



print(sum / len(d))