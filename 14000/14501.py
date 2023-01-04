import sys
n = int(sys.stdin.readline())
val = [(0,0)]
dp = [0] + [0]*n

for i in range(n):
    t, p = map(int, sys.stdin.readline().split())
    val.append((t, p))

for i in range(1, n+1):
    if val[i][0]+i-1 <= n:
        dp[val[i][0]+i-1] = max(val[i][1]+dp[i-1], dp[val[i][0]+i-1])
        for j in range(val[i][0]+i-1, n+1):
            if dp[val[i][0]+i-1] > dp[j]:
                dp[j] = dp[val[i][0]+i-1]
print(dp[-1])