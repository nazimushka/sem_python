# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

lst = '1 0 4 5 6.4 7.8'

l = [float(i) for i in lst.split()]
print(min(l), max(l))
