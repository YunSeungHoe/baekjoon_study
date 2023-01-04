import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n, num = map(int, sys.stdin.readline().split())
    for _ in range(num):
        start, end = map(int, sys.stdin.readline().split())
    print(n-1)