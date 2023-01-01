import sys
n = int(sys.stdin.readline())
r = []
g = []
b = []
for _ in range(n):
    x, y, z = map(int, sys.stdin.readline().split())
    r.append(x)
    g.append(y)
    b.append(z)

for i in range(1, n):
    r[i] = min(g[i-1], b[i-1]) + r[i]
    g[i] = min(r[i-1], b[i-1]) + g[i]
    b[i] = min(r[i-1], g[i-1]) + b[i]
print(min(r[n-1], g[n-1], b[n-1]))