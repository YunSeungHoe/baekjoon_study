n = int(input())
num = list(map(int, input().split()))
num.sort()
sum = 0
for i in range(n+1):
    for j in range(i):
        sum += num[j]
print(sum)