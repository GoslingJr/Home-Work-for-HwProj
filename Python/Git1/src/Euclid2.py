def extended_gcd(a, b):
    """
    Расширенный алгоритм Евклида.
    Возвращает кортеж (g, x, y), где g = gcd(a, b),
    а также такие x и y, что a*x + b*y = g.
    """
    if b == 0:
        return (a, 1, 0)
    else:
        g, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (g, x, y)

# Ввод числа a
a_input = input("Введите число a: ")
b_input = input("Введите число b: ")

try:
    a = int(a_input)
    b = int(b_input)
except ValueError:
    print("Ошибка: необходимо вводить целые числа.")
    exit()

# Проверка на отрицательные числа и преобразование
if a < 0:
    print("Число a отрицательное. Берем его абсолютное значение.")
    a = abs(a)

if b < 0:
    print("Число b отрицательное. Берем его абсолютное значение.")
    b = abs(b)

# Теперь вычисляем НОД и коэффициенты
g, x, y = extended_gcd(a, b)

print(f"НОД({a}, {b}) = {g}")
print(f"Рассмотрение соотношения Безу: {a}*({x}) + {b}*({y}) = {g}")