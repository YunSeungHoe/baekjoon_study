n = int(input())
for i in range(n):
    num, str = input().split()
    num = int(num)
    str = list(str)
    str.pop(num-1)
    print(''.join(str))