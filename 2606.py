import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
net = dict()
visit = set()
queue = [1]

for i in range(n): net[i+1] = list()

for _ in range(m):
    key, val = map(int, sys.stdin.readline().split())
    if key > val: key, val = val, key
    temp = net[key]
    temp.append(val)
    net[key] = temp

while len(queue) != 0:
    start = queue.pop(0)
    if start in visit: continue
    visit.add(start)
    for i in net[start]: queue.append(i)

print(len(visit)-1)