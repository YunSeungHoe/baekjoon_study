n = int(input())
t = []
w = []
result = []

for i in range(n):
    x, y = map(int, input().split())
    w.append(x)
    t.append(y)

for i in range(n):
    count = 1
    for j in range(n):
        if i == j:
            continue
        if w[i] < w[j] and t[i] < t[j]:
            count += 1
    result.append(count)

print(*result)