n = int(input())
star = '*'
space = ' '
for i in range(2*n-1):
    a = abs(i - n + 1)
    b = abs(2*i - (2*n - 2))
    print(star*abs(a - n)+space*b+ star*abs(a -n))