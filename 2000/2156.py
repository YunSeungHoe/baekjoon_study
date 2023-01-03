import sys
n = int(sys.stdin.readline())
val = [0]
dp = [0]
for _ in range(n):
    val.append(int(sys.stdin.readline()))
if n == 1:
    print(val[1])
elif n == 2:
    print(val[1] + val[2])
else:
    dp.append(val[1])
    dp.append(val[1] + val[2])
    for i in range(3, n+1):
        dp.append(max(dp[i-1], dp[i-2] + val[i], dp[i-3] + val[i-1] + val[i]))
    print(dp[n])