import sys
n = int(sys.stdin.readline())
num = []
num2 = [0] * 8001
for _ in range(n):
    temp = int(sys.stdin.readline())
    num.append(temp)
    temp += 4000
    num2[temp] += 1


print(round(sum(num)/n))
num = sorted(num)
print(num[n//2])
m = 0
for i in range(len(num2)):
    if num2[i] > m:
        m = num2[i]
max_val = []
for i in range(len(num2)):
    if m == num2[i]:
        max_val.append(i)
if len(max_val) == 1:
    print(max_val[0] - 4000)
else:
    print(max_val[1] - 4000)
    
print(max(num) - min(num))