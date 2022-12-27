import sys
n, s = map(int, sys.stdin.readline().split())
coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline()))

cnt = 0
while len(coin) != 0:
    temp = coin.pop()
    if temp <= s:
        cnt += s // temp
        s = s - temp*(s//temp)
    if s == 0:
        break
print(cnt)