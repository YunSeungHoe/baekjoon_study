a, b, c = map(int, input().split())
if a*b == b*c+a: print(0)
elif a*b > b*c+a: print(2)
else: print(1)