a, b = map(int, input().split())
num = list(map(int, input().split()))
result = []
for i in num:
    result.append(i - a*b)
print(*result)