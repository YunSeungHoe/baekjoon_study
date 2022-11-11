import sys
input = sys.stdin.readline

n = int(input())
min = 5000
for i in range(0, n+1):
    if i*3 > n:
        if min != 5000: print(int(min))
        else: print(-1)   
        break
    else:
        if (n - i*3) % 5 == 0:
            if min > i + (n - i*3)/5:
                min = i + (n - i*3)/5