# №2 Напишите программу, которая будет на вход
# принимать число N и выводить числа от -N до N
# Примеры:
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# #первый способ
# N = int(input('Введите чилсо N = '))
# nums = []
# for i in range(-N, N+1, 1):
#     nums.append(i)
# print(nums)

# # второй способ
# N = int(input('Введите чилсо N = '))
# for i in range(-abs(N), abs(N)+1, 1):
#     print(i)

# второй способ (добавили параметр отображения принта)
N = int(input('Введите чилсо N = '))
for i in range(-abs(N), abs(N)+1, 1):
    print(i, end=' ')
