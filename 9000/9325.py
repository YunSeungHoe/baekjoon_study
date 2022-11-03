a = int(input())
for i in range(a):
    car = int(input())
    b = int(input())
    for j in range(b):
        q, p = map(int, input().split())
        car += q * p
    print(car)