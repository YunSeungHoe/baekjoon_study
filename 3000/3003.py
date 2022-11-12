all = [1, 1, 2, 2, 2, 8]
n = list(map(int, input().split()))
result = []
for i in range(len(all)):
    result.append(all[i] - n[i])
print(*result)