# 34 В файле находится N натуральных чисел,
# #записанных через пробел. Среди чисел не #хватает одного,
# чтобы выполнялось условие
# #A[i] - 1 = A[i-1]. Найдите это число.


with open('34file.txt', 'r') as file:
    numbers = list(map(int, file.read().split()))
print(numbers)

for i in range(1, len(numbers)):
    if (numbers[i] - numbers[i - 1]) > 1:
        print(numbers[i] - 1)
        numbers.insert(i, numbers[i - 1] + 1)

print(numbers)

with open('file.txt', 'w') as file:
    # print(*numbers, file=file, sep=' ')
    file.write(' '.join(list(map(str, numbers))))


# # Второй
# with open('For_seminar_5.txt', 'r') as f:
#     nums = list(map(int,f.read().split()))
#     print (nums)

# for i in range (1, len(nums)):
#     if (nums[i]-nums[i-1])>1:
#         nums.insert(i, nums[i-1]+1)

# print (nums)

# data = open('For_seminar_5.txt', 'w')
# data.write(' '.join(list(map(str,nums))))
# data.close()
