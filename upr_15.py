def test(a):
    return a ** 2

def calc(op, a, b):
    switch = {
        "add": lambda a, b: a + b,
        "sub": lambda a, b: a - b,
        "mul": lambda a, b: a * b,
        "div": lambda a, b: a / b if b != 0 else None,
        "mod": lambda a, b: a % b,
        "test": lambda a, b: test(a),
    }
    return switch[op](a, b)

if __name__ == "__main__":
    print(calc("add", 1, 2))
    print(calc("sub", 1, 2))
    print(calc("mul", 1, 2))
    print(calc("div", 1, 0))
    print(calc("mod", 1, 2))
    print(calc("test", 2, 2))


# Аналог на switch / casa
x = 3
match x:
    case 3:
        print(f" X = {x}")