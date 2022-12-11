# №9 Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# ax = int(input('Введите координату AX:'))
# ay = int(input('Введите координату AY:'))
# bx = int(input('Введите координату BX:'))
# by = int(input('Введите координату BY:'))

# sqrt = ((bx-ax)**2+(by-ay)**2)**0.5
# print(sqrt)

# # УЛУЧШЕНИЕ:

firstPoint = list(map(int, input(
    "Введите координаты первой точки x y z через пробел:").split()))
secondPoint = list(map(int, input(
    "Введите координаты второй точки x y z через пробел:").split()))
result = (((secondPoint[0] - firstPoint[0])**2) + ((secondPoint[1] -
          firstPoint[1])**2) + ((secondPoint[2] - firstPoint[2])**2))**(1/2)
print(f"Расстояние между двумя точками пространства = {round(result, 2)}")
