l = [6, 4, 2, 3]

l.append(7)
print(l)
l.pop()
print(l)
# l.pop(0)
# print(l)

print(len(l))
l.reverse()
print(l)
l.sort()
print(l)

print(l)
l.reverse()
l.insert(0, 22)
print(l)


for i in l:
    print(i, end=" - ")