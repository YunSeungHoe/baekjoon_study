# using pypy3
import sys
row, col, b = map(int, sys.stdin.readline().split())
m = []
for _ in range(row):
    m.append([int(x) for x in sys.stdin.readline().rstrip().split()])
    
min_time = sys.maxsize
min_h = 0
for i in range(257):
    min_target = 0
    max_target = 0
    for j in m:
        for k in j:
            if k >= i:
                max_target += k - i
            else:
                min_target += i - k
    if min_target > max_target + b:
        continue
    cnt = min_target + (max_target * 2)
    if cnt <= min_time:
        min_time = cnt
        min_h = i
print(min_time, min_h)