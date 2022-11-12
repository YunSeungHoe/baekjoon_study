x = int(input())
for _ in range(x):
    a = input() 
    print(a)
    a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = map(int, a.split())
    if 17 in (a1, a2, a3, a4, a5, a6, a7, a8, a9, a10):
        if 18 in (a1, a2, a3, a4, a5, a6, a7, a8, a9, a10): print('both')
        else: print('zack')
    else:
        if 18 in (a1, a2, a3, a4, a5, a6, a7, a8, a9, a10): print('mack')
        else: print('none')
    if _ != x-1: print()