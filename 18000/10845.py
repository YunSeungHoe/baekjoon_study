import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    str = list(input())
    w = "".join(str[0:4])
    if w == 'push':
        num = int("".join(str[5: len(str)]))
        arr.append(num)
    elif w == 'back':
        if len(arr) == 0: print(-1)
        else: print(arr[len(arr)-1])
    elif w == 'size':
        print(len(arr))
    elif "".join(str[0:3]) == 'pop':
        if len(arr) == 0: print(-1)
        else: 
            print(arr[0])
            arr.pop(0)
    elif "".join(str[0:5]) == 'front':
        if len(arr) == 0: print(-1)
        else: print(arr[0])
    elif "".join(str[0:5]) == 'empty':
        if len(arr) == 0: print(1)
        else: print(0)