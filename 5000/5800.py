n = int(input())
for i in range(n):
    x = list(map(int, input().split()))
    gap = 0
    up = max(x[1:])
    down = min(x[1:])
    x = x[1:]
    x.sort()
    for k in range(1, len(x)):
        if abs(x[k-1] - x[k]) > gap:
            gap = abs(x[k-1] - x[k])
    print("Class", i+1)
    print("Max {}, Min {}, Largest gap {}".format(up, down, gap))