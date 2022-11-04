max = 0
cur = 0
for x in range(10):
    o, i = map(int, input().split())
    cur += i-o
    if max < cur:
        max = cur
print(max)