n = int(input())
star = '*'
space = ' '
for i in range(n):
    print(space*(n-i-1) + star*(2*i+1))