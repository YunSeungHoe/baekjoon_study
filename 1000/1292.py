a = []
n, m = map(int, input().split())
for i in range(1, m):
    for j in range(i):
        a.append(i)
if m == 1:
    print(1)
elif m == 2:
    print(3)
else:
    print(sum(a[n-1:m]))