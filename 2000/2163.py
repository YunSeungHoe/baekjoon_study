r, c = map(int, input().split())
if r == 1 and c == 1:
    print(0)
else:
    print(r*c - 1)