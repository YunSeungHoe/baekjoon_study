n = int(input())
star = '*'
space = ' '
for i in range(n):
    print(space*(i) + star*(2*(n-i)-1))