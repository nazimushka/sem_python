# 38 Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
#     *Пример:*
#     2+2 => 4;
#     1+2*3 => 7;
#     1-2*3 => -5;


# # первый вариант
# line = input("Введите выражение: ")
# line = line.split()
# print(line)
# result = 0


# def op(ch, line1):
#     for i in range(1, len(line1) - 1):
#         if line1[i] == ch:
#             if ch == "*":
#                 line1[i - 1] = int(line1[i - 1]) * int(line1[i + 1])
#             elif ch == "/":
#                 line1[i - 1] = int(line1[i - 1]) / int(line1[i + 1])
#             elif ch == "+":
#                 line1[i - 1] = int(line1[i - 1]) + int(line1[i + 1])
#             elif ch == "-":
#                 line1[i - 1] = int(line1[i - 1]) - int(line1[i + 1])
#             line1.pop(i + 1)
#             line1.pop(i)
#             break
#     return line1


# while len(line) > 1:
#     if line.count("*"):
#         line = op("*", line)
#     elif line.count("/"):
#         line = op("/", line)
#     elif line.count("+"):
#         line = op("+", line)
#     elif line.count("-"):
#         line = op("-", line)

# print(line[0])

# Признаюсь, данное решение подглядел, но разобрал, поскольку модуль re показался очень любытным и захотелось поподробнее узнать

import re

actions = {
    "^": lambda x, y: str(float(x)**float(y)),
    "*": lambda x, y: str(float(x) * float(y)),
    "/": lambda x, y: str(float(x) / float(y)),
    "+": lambda x, y: str(float(x) + float(y)),
    "-": lambda x, y: str(float(x) - float(y))
}

priority_reg_exp = r"\((.+?)\)"
action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"


def my_eval(expresion: str) -> str:

    while (match := re.search(priority_reg_exp, expresion)):
        expresion: str = expresion.replace(
            match.group(0), my_eval(match.group(1)))

    for symbol, action in actions.items():
        while (match := re.search(action_reg_exp.format(symbol), expresion)):
            expresion: str = expresion.replace(
                match.group(0), action(*match.groups()))

    return expresion


exp = "1-2*3"
print(my_eval(exp), eval(exp))
