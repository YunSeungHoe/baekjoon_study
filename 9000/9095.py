def add_123(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 4
    return add_123(x-1) + add_123(x-2) + add_123(x-3)

import sys
n = int(sys.stdin.readline())

for _ in range(n):
    x = int(sys.stdin.readline())
    print(add_123(x))