import sys
k, n = map(int, input().split())
have = [int(sys.stdin.readline()) for _ in range(k)]
s = 1
e = max(have)

while(s<=e):
    mid = (s+e) // 2
    lines = 0
    for i in have:
        lines += i//mid
    if lines>=n:
        s = mid + 1
    else:
        e = mid - 1
print(e)