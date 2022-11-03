n = int(input())

for i in range(n):
    x = int(input())
    all = 0
    sum = 0
    for j in range(x):
        sub, score = input().split()
        sum += float(sub) * float(score)
        all += int(sub)
    print(all, round(sum/all, 1))