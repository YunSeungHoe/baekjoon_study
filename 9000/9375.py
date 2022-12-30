import sys
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    dress = {}
    for _ in range(n):
        val, key = map(str, sys.stdin.readline().strip().split())
        if key in dress:
            dress[key].append(val)
        else:
            dress[key] = [val]
    cnt = 1
    for i in dress:
        cnt *= (len(dress[i])+1)
    print(cnt-1)