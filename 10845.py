n = int(input())
arr = []
for _ in range(n):
    str = list(input())
    if str[0] == 'p' and str[1] == 'u':
        num = int("".join(str[5: len(str)]))
        arr.append(num)
    elif str[0] == 'f':
        if len(str) == 0: print(-1)
        else: print(arr[0])
    elif str[0] == 'b':
        if len(str) == 0: print(-1)
        else: print(arr[len(arr)-1])
    elif str[0] == 's':
        print(len(arr))
    elif str[0] == 'p' and str[1] == 'o':
        if len(arr) == 0: print(-1)
        else: 
            print(arr[0])
            arr.pop(0)
    elif str[0] == 'e':
        if len(arr) == 0: print(1)
        else: print(0)