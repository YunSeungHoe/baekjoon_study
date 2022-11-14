p, m = map(int, input().split())
if  p + m < 0 or p - m < 0 or (p + m) % 2: print(-1)
else:
    a = (p + m) // 2
    b = p - a
    print(max(a, b), min(a, b))