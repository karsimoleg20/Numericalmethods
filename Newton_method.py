import math

# Початкова функція
def equation(x):
    return x**2 * math.log(x, 10) - 1  # Повернуто math.log(x, 10)

# Похідна функції
def derivative(x):
    return 2 * x * math.log(x, 10) + x  # Повернуто math.log(x, 10)

# Реалізація методу
def modified_newton_method(f, df, x0, tol=1e-6, max_iter=100):
    x = x0          # Початкове наближення для кореня.
    iteration = 0   # Лічильник ітерацій.

    while abs(f(x)) > tol and iteration < max_iter:
        # Повторюємо ітерації, доки не досягнемо точності tol або не перевищимо максимальну кількість ітерацій
        x = x - f(x) / df(x)   # Обчислюємо нове наближення кореня
        iteration += 1         # Збільшуємо лічильник ітерацій на одиницю
        fx = f(x)              # Обчислюємо значення функції f(x) на поточній ітерації
        print(f"Iteration {iteration}: x = {x}, f(x) = {fx}")

    return x, iteration  # Повертаємо знайдений наближений корінь та кількість ітерацій


x0 = 1.0  # Значення початкового наближення

# Збільшуємо кількість ітерацій
root, iterations = modified_newton_method(equation, derivative, x0, max_iter=12)

# Виводимо результати на екран
print(f"Кількість ітерацій: {iterations}")