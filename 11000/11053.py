import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
val = [0]*n
for i in range(n):
    for j in range(i):
        if num[i] > num[j] and val[i] < val[j]:
            val[i] = val[j]
    val[i] += 1
print(max(val))