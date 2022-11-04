import sys
sys.setrecursionlimit(1002)
def func(n):
    sum = 0
    if n == 1:
        return 3
    for i in range(n+1):
        sum = sum + n + i 
    return sum + func(n-1)

n = int(input())
print(func(n))