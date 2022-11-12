a, b =map(int, input().split())
result = (a / 100) * b
if a-result >= 100: print(0)
else: print(1) 