arr = ['a', 'b', 'c', 'd', 'e', 'f',
       'g', 'h', 'i', 'j', 'k', 'l',
       'm', 'n', 'o', 'p', 'q', 'r',
       's', 't', 'u', 'v', 'w', 'x',
       'y', 'z']
num = [0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0,
       0, 0]
str = list(input())
for i in range(len(str)):
    for j in range(len(arr)):
        if str[i] == arr[j]:
            num[j] += 1
            break
print(*num)