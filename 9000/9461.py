t = int(input())
for _ in range(t):
    temp = [ 1, 1, 1, 2, 2]
    n = int(input())
    for i in range(6, n+1):
        temp.append(temp[i-2] + temp[i-6])
    print(temp[n-1])