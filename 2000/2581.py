min1 = int(input())
max = int(input())
val = []
for i in range(min1, max+1):
    flag = True
    if i == 1: continue
    elif i == 2: val.append(i)
    for j in range(2, i):
        if i % j == 0:
            break
        elif j == i - 1:
            val.append(i)
if len(val) == 0:
    print(-1)
else: 
    print(sum(val))
    print(min(val))