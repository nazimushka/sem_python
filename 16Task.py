# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.


from random import randint         # из библиотеки random, нужна одна функция под названием randint.


list = []                          # Создали список
f = open('16file.txt', 'r')        # Отркыли файл
n = int(input('Введите n:'))       # Вписали n
count = 1                          # Создали счетик
list_f = f.readlines()             # Создали список из всех строчек file.txt
f.close()                          # Файл закрыли
for i in range(0, n):              # Заполнили наш список случайными числами
    list.append(randint(-n, n))

for i in range(len(list_f)):       # Через ложный цикл удаляем '/' и 'n'
    for j in (list_f[i]):
        if j == '/' or j == 'n':
            j = ''

for i in list_f:                   # по нашему измененному списку мы идем. Позиции преобразовываем в число

    count *= list[int(i)]

print(list)
print(count)