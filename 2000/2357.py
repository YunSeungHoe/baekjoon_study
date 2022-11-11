import math
import sys
input = lambda: sys.stdin.readline().rstrip()
def make(index, x, y):
    if x == y:
        seg[index] = (val[x], val[x])
        return seg[index]
    mid = (x + y) // 2 
    l = make(index*2, x, mid)
    r = make(index*2+1, mid+1, y)
    seg[index] = (min(l[0], r[0]), max(l[1], r[1]))
    return seg[index]

def func(index, x, y):
    if y < a or b < x:
        return(1000000000, 0)
    mid = (x + y) // 2
    if a <= x and y <= b:
        return seg[index]
    else:
        l = func(index*2, x, mid)
        r = func(index*2+1, mid+1, y)
        return (min(l[0], r[0]), max(l[1], r[1]))

n, m = map(int, input().split())
val = [int(input()) for _ in range(n)]
b = math.ceil(math.log2(n)) + 1
depth = 1 << b
seg = [0 for _ in range(depth)]
make(1, 0, len(val)-1)

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    result = func(1, 0, len(val)-1)
    print(result[0], result[1])