"""
Вычисление факториала

Факториалом числа называют произведение всех натуральных
чисел до него включительно.

Например, факториал числа 5 равен произведению 1 * 2 * 3 * 4 * 5 = 120.

Формула нахождения факториала:
n! = 1 * 2 * … * n, где n – это число, а n! – факториал этого числа.
"""
import math


# def factorial(n: int) -> int:          #Первое решение
#     return math.factorial(n)

# def factorial(n: int) -> int:         #Второе ршение
#     if n == 0:
#         return 1
#     return factorial(n - 1) * n

def factorial(n: int) -> int:           #Третье решение
    factarial = 1

    for i in range(2, n + 1):
        factarial *= i

    return factarial








if __name__ == '__main__':
    assert factorial(5) == 120
    print('Решено!')
