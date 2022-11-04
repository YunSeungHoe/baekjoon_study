n = int(input())
x = []
for i in range(n+1):
    if i == 0 or i == 1:
        x.append(i)
    else:
        x.append(x[i-1]+x[i-2])
print(x[-1])