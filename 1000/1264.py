word = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
while True:
    arr = list(input())
    cnt = 0
    if len(arr) == 1 and arr[0] == '#':
        break
    else:
        for i in arr:
            if i in word:
                cnt += 1
        print(cnt)