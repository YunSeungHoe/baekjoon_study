n = int(input())
star = '*'
for i in range(2*n - 1):
    a = abs(i-(n-1))
    print(star*abs(a - n))
    