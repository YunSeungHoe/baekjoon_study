n = int(input())
x = 1
while(1):
    if 2*n < x*x + x:
        break
    x += 1
print(x-1)