one, n, money = map(int, input().split())

if one * n <= money:
    print(0)
else:
    rev = abs(money - one*n) 
    print(rev)