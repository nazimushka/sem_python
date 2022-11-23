# №6 Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

X = int(input('Введите значение предикат X: '))
Y = int(input('Введите значение предикат Y: '))
Z = int(input('Введите значение предикат Z: '))


def trfl(X, Y, Z):
    if not (X or Y or Z) == (not X) and (not Y) and (not Z):
        return True
    else:
        return False


print(trfl(X, Y, Z))
