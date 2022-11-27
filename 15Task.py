# 15 Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.
#     *Пример:*
# - Для n = 3:  {1: 2, 2: 2.25 , 3: 2.37}
# Необходимо сложить все значения словаря и вывести  сумму на экран.

n = int(input('Введите n: '))     # ввели  число
score = {}                        # пустой словарь
count=0                           # счетчик

for i in range (1, n + 1 ):       # цикл for
    score[i] = (1+(1/i)) ** i     # заполняем словарь
    count += score[i]             # считаем сумму

print(score)                      # Словарь 
print(count)                      # Сумма