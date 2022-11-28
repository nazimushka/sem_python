# Реализуйте алгоритм нахождения(генерации) рандомного(случайного) числа.
# (Не используя библиотеки связанные с рандомом)

import datetime

randomNum = datetime.datetime.now().microsecond%10

print (f'Случайное число: {(randomNum) }')
