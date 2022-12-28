n, m = map(int, input().split())
d = {}
for _ in range(n):
    home, pwd = input().split()
    d[home] = pwd
for _ in range(m):
    home = input()
    print(d[home])