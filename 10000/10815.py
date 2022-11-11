from collections import deque

my = int(input())
mycard = list(map(int, input().split()))

you = int(input())
youcard = list(map(int, input().split()))

def binary(my, val, start, end):
    while start <= end:
        mid = (start + end) // 2
        if val == my[mid]:
            return 1
        elif val < my[mid]:
            end = mid - 1
        elif val > my[mid]:
            start = mid + 1
    return 0


mycard.sort()
for i in range(len(youcard)):
    if binary(mycard, youcard[i], 0, my - 1) == 1:
        print(1, '', end="")
    else:   
        print(0, '', end="")
        