for i in range(3):
    val = list(map(int, input().split()))
    n = sum(val)
    if n == 3: print('A')
    elif n == 2: print('B')
    elif n == 1: print('C')
    elif n == 0: print('D')
    elif n == 4: print('E')
    