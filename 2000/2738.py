n, m = map(int, input().split())
a = []
b = []
t = []
s = []
for _ in range(n): a.append(list(map(int, input().split())))
for _ in range(n): b.append(list(map(int, input().split())))

for i in range(n):
    t = []
    for j in range(m):
        t.append(a[i][j] + b[i][j])
    s.append(t)

for i in range(n):
    print(*s[i])