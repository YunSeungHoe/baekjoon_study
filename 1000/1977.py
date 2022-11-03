min = int(input())
max = int(input())
temp = []
i = 1
while(i**2 <= max):
    if min <= i*i <= max:
        temp.append(i**2)
    i += 1
if temp == []:
    print(-1)
else:
    print(sum(temp))
    print(temp[0])