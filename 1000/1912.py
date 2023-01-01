import sys 
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
val = [num[0]]
for i in range(1, n):
    val.append(max(val[i-1]+num[i], num[i]))
print(max(val))