n = int(input())
star = '*'
space = ' '
sstar = '* '
for i in range(n):
    print(space*(n-i-1) + sstar*i + star)