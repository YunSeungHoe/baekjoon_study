import math 
n = int(input())
for i in range(n):
    h, w, x = map(int, input().split())
    first = x % h
    if first == 0:
        first = h
    second = math.ceil(x/h)
    print(first*100 + second)