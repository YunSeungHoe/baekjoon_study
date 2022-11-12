n = int(input())
result = []
for _ in range(0, n, 4):
    result.append("long")
result.append("int")
print(*result)