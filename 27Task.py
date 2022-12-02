# Найдите корни квадратного уравнения Ax² + Bx + C = 0

str1 = '- 4 * x^2 + 3 * x - 8 = 0'
nums = str1.split()

nums1 = []
for i in nums:
    if i.isdigit() or i == '-':
        nums1.append(i)
    if i == '=':
        break
print(nums1)

i = 0
while nums1.count('-') != 0:
    if nums1[i] == '-':
        nums1[i] += nums1[i + 1]
        nums1.pop(i + 1)
        i = 0
    i += 1
print(nums1)

a, b, c = int(nums1[0]), int(nums1[1]), int(nums1[2])

# exit()

d = b ** 2 - 4 * a * c
if d < 0:
    print('no roots')
elif d == 0:
    print(round(- b / (2 * a), 2))
else:
    print(round((- b + (d ** 0.5)) / (2 * a), 2))
    print(round((- b - (d ** 0.5)) / (2 * a), 2))
