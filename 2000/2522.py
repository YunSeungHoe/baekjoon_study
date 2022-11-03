n = int(input())
star = '*'
space = ' '
for i in range(2*n - 1):
    a = abs(i-(n-1))
    print(space*abs(i - n + 1)+star*abs(a - n))
    