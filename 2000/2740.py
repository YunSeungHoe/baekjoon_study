n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
        
m, k = map(int, input().split())
b = []
for i in range(m):
    b.append(list(map(int, input().split())))

result = []
for x in range(n):
    for y in range(k):
        temp = 0
        for z in range(m):
            temp += a[x][z]*b[z][y]
        result.append(temp)

for i in range(n):
    print(*result[k*i:k*(i+1)])