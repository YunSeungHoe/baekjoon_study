n = int(input())
val = list()
for i in range(n):
    if i == 0:
        val.append(1)
    elif i == 1:
        val.append(3)
    else:
        val.append(val[i-1] + val[i-2]*2)
print(val[n-1]%10007)