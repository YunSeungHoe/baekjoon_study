n = int(input())
star = '*'
space = ' '
for i in range(2*n - 1):
    a = abs(2*i-2*(n-1))
    print(space*abs(n-i-1) + star*(2*n - 1 - a))