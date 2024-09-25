import math

a = -0.75
b = 0.25
x = -0.25
accuracy = 10 ** -4
q = 0.73
iterations_dichotomy = 13
iterations_simple = 33
stop_iteration = None

def dichotomy_method():
    global a, b, x

    print(f"{'Ітерація':^8}|{'a':^18}|{'b':^18}|{'x':^18}|{'f(x)':^18}")
    print('-' * 80)

    for i in range(iterations_dichotomy + 1):
        if i == iterations_dichotomy:
            print(f"{i:^8}|{a:^18.8f}|{b:^18.8f}|{x:^18.8f}|{'---':^18}")
            break

        fx = compute_value_dichotomy(x)

        print(f"{i:^8}|{a:^18.8f}|{b:^18.8f}|{x:^18.8f}|{fx:^18.8f}")

        fa = compute_value_dichotomy(a)

        if math.copysign(1, fx) == math.copysign(1, fa):
            a = x
        else:
            b = x

        x = (a + b) / 2


def iteration_method():
    global x, stop_iteration

    print(f"{'Ітерація':^10}|{'x':^20}|{'AO':^20}")
    print('-' * 52)

    print(f"{0:^10}|{x:^20.8f}|{'---':^20}")

    for i in range(1, iterations_simple + 1):
        previous_x = x
        x = compute_value_iteration(x)
        ao = (1 / (1 - q)) * abs(x - previous_x)

        print(f"{i:^10}|{x:^20.8f}|{ao:^20.8f}")

        if ao < accuracy and stop_iteration is None:
            stop_iteration = i

    print("")

    if stop_iteration:
        print(f"Ми могли зупинитися ще на {stop_iteration}-й ітерації.")

def compute_value_dichotomy(x):
    return x ** 2 + math.sin(x) - 12 * x - 0.25

def compute_value_iteration(x):
    return (16 * (x ** 3) - 112 * x - 4 * (x ** 2) - 4 * math.sin(x) + 1) / (16 * (x ** 2) - 160)

def main():
    print("")
    print("Оберіть метод рішення нелінійного рівняння:")
    print("")
    print("1 - Метод дихотомії")
    print("2 - Метод простої ітерації")
    print("")

    choice = input("Введіть номер метода (1 чи 2): ")

    if choice == '1':
        dichotomy_method()
    elif choice == '2':
        iteration_method()
    else:
        print("Некоректний ввод. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
