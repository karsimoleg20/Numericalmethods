import math

# Точність
epsilon = 1e-4

# Мінімальне та максимальне значення x
rangeMin = 0.1
rangeMax = 2.4

# Крок ітерації
step = 0.01

# Початкова функція
def equation(x):
    return x**2 * math.log(x) - 1

# Функція для форматування чисел з фіксованою точністю
def to_fixed(num):
    return f"{num:.10f}"

# Метод релаксації
def relaxationMethod():
    # Ініціалізуємо мінімум та максимум
    min1 = float('inf')
    max1 = float('-inf')

    # Початкове значення x
    x = rangeMin
    previous_x = None

    # Знаходимо мінімум та максимум функції в заданому діапазоні
    while x <= rangeMax:
        y = equation(x)
        min1 = min(min1, y)
        max1 = max(max1, y)
        x += step

    # Виводимо мінімум та максимум на екран
    print("Min: ", min1, "Max: ", max1)

    # Початкове наближення x
    x = rangeMin

    # Значення z0 для розрахунку кількості ітерацій
    z0 = abs(x)

    # Розрахунок константи q та початкового значення t0
    q = (max1 - min1) / (max1 + min1)
    t0 = 2 / (max1 + min1)

    # Розрахунок кількості ітерацій n
    n = abs(int(math.log(abs(z0) / epsilon) / math.log(1 / q))) + 1

    # Початкове значення функції на початковому наближенні
    fx = equation(x)
    it_amount = 0

    # Застосовуємо метод релаксації
    while it_amount < n:
        x = x - t0 * equation(x)
        fx = equation(x)
        it_amount += 1

        print(f"Iteration {it_amount}: x = {to_fixed(x)} f(x) = {to_fixed(fx)}")

# Викликаємо метод релаксації для знаходження кореня
relaxationMethod()