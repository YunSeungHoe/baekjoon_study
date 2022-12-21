n = int(input())
my = list(map(int, input().split()))
m = int(input())
card = list(map(int, input().split()))
mydic = {}
ret = []

for i in my:
    if i in mydic: mydic[i] += 1
    else: mydic[i] = 1
for i in card:
    if i in mydic: ret.append(mydic[i])
    else: ret.append(0)
print(*ret)