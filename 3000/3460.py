def find(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    for i in range(1, n):
        if pow(2, i) > n:
            return i-1

n = int(input())

for k in range(n):
    m = int(input())
    result = []
    msb = find(m)
    for i in range(msb, -1, -1):
        temp = pow(2, i)
        if m >= temp:
            m -= temp
            result.append(i)
    val = sorted(result)
    print(*val)