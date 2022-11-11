sum = 0
num = [9, 7, 8, 0, 9, 2, 1, 4, 1, 8]
for _ in range(3): num.append(int(input()))

for i in range(len(num)):
    if i % 2 == 0:
        sum += num[i] * 1
    else:
        sum += num[i] * 3
print("The 1-3-sum is",sum)