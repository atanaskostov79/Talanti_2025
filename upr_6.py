
a = ""
l = []

while a != 0:
    a = int(input("Enter number: "))
    if a == 0:
        break
    l.append(a)
s = 0
for x in l:
    s = s + x
print(s)


print(sum(l))