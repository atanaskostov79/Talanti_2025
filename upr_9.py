d = { 1: "Alex",
      2: "Bob",
      3: "Charlie",
      }


for x in d.values():
    print(x)
for x in d.keys():
    print(x)

k = 7
if k in d.keys():
    d.pop(k)
    print("Key exists")
else:
    print("Key does not exist")
    # d[3] = "Mitok"
d.popitem()
for x,y in d.items():
    print(f" {x} , {y}")
# print(d[1])