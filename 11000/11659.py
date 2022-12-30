import sys
n, t = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
for i in range(n-1):
    num[i+1] += num[i]
num = [0] + num
for _ in range(t):
    s, e = map(int, sys.stdin.readline().split())
    print(num[e] - num[s-1])