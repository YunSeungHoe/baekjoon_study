n = int(input())
result = []
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            result.append((i, j))
result = set(result)
result = list(result)
print(len(result))