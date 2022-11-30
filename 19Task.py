# 19 Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.

# lst = ['blue', 'green', 'white', 'gr2y', 'red']
# num = 5
# answer = False
# for i in lst:
#     for j in i:
#         if j == str(num):
#             answer = True
#             break
# print(answer)

lst = ['blue', 'green', 'white', 'gr2y', 'red']
num = 2
answer = False

for i in lst:
    if i.count(str(num)):
    # if str(num) in i:
        answer = True
        break
    # for j in i:
    #     if j == str(num):
    #         answer = True
    #         break
print(answer)
