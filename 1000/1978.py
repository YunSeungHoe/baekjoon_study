n = int(input())
num = list(map(int, input().split()))
result = 0
for i in range(n):
    flag = True
    if num[i] == 1:
        result -= 1
    for j in range(2, num[i]):
        if num[i] % j == 0:
            flag = False
            break
    if flag: result += 1
print(result)