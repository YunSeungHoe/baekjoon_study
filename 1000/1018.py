r, c = map(int, input().split())
m = []
result = []
for _ in range(r):
    m.append(list(input()))

for i in range(r-7):
    for j in range(c-7):
        draw1 = 0
        draw2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if m[a][b] == 'W':
                        draw1 += 1
                    elif m[a][b] == 'B':
                        draw2 += 1
                else:
                    if m[a][b] == 'W':
                        draw2 += 1
                    elif m[a][b] == 'B':
                        draw1 += 1
        result.append(draw1)
        result.append(draw2)
print(min(result))