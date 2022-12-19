n = int(input())
for i in range(0, n+1):
    temp = list(map(int, str(i)))
    if sum(temp)+i == n:
        print(i)
        break
    if i == n:
        print(0)