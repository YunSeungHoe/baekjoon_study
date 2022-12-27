import sys, copy

t = int(sys.stdin.readline())
for _ in range(t):
    row, col, n = map(int, sys.stdin.readline().split())
    temp = []
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        temp.append((x, y))
    
    cnt = 0
    rem = []
    while len(temp) != 0:
        val = temp.pop(0)
        rem.append(val)
        while len(rem) != 0:
            val = rem.pop(0)
            if (val[0] + 1, val[1]) in temp:
                temp.remove((val[0] + 1, val[1]))
                rem.append((val[0] + 1, val[1]))
            if (val[0] - 1, val[1]) in temp:
                temp.remove((val[0] - 1, val[1]))
                rem.append((val[0] - 1, val[1]))
            if (val[0], val[1] + 1) in temp:
                temp.remove((val[0], val[1] + 1))
                rem.append((val[0], val[1] + 1))
            if (val[0], val[1] - 1) in temp:
                temp.remove((val[0], val[1] - 1))
                rem.append((val[0], val[1] - 1))
        cnt += 1
    print(cnt)                