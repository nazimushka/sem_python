# 31 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)*
# многочлена и записать в файл многочлен степени k.
#     *Пример:*
#     - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#     - k=5 => 2*x^5 + 4*x^4 + 2*x^3 + 2*x^2 + 4*x + 5 = 0
# *Доп задание: значения коэффициентов от -100 до 100.


import random

k = int(input('Введите число k = '))
coef = [random.randint(-100, 100) for i in range(0, k+1)]


def Polynom(k, koef):
    pol = ''
    for i in range(0, k+1):
        if k - i > 1 and coef[i] != 0:
            pol += f'{coef[i]}*x^{k-1} + '
        elif k-1 == 1 and coef[i] != 0:
            pol += f'{coef[i]}*x + '
        elif coef[i] == 0:
            pol += ''
        else:
            pol += f'{coef[i]} = 0'
    return pol


with open('31file.txt', 'w') as data:
    data.write(Polynom(k, coef).replace('+ -', '- '))
