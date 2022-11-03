n = int(input())
max = 0
for i in range(n):
    a, b, c = map(int, input().split())
    if a == b and b == c:
        money = 10000 + a*1000
    elif a == b:
        money = 1000 + a*100
    elif b == c:
        money = 1000 + b*100
    elif c == a:
        money = 1000 + c*100
    else:
        if a > b and a > c:
            money = a*100
        elif b > a and b > c:
            money = b*100
        else:
            money = c*100
    if money > max:
        max = money
print(max)