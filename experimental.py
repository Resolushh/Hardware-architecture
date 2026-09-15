def experiment(a):
    print(f"Число: {a}")
    print(f"В двоичном виде: {bin(a)}")
    print()

    print(f"a & 1  = {a & 1}")
    print(f"a | 1  = {a | 1}")
    print(f"a ^ 1  = {a ^ 1}")
    print(f"~a     = {~a}")
    print(f"a << 1 = {a << 1}")
    print(f"a >> 1 = {a >> 1}")


a = int(input("Введите число: "))
experiment(a)