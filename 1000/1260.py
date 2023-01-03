import sys, copy

def dfs(d, s):
    queue = []
    visit = []
    queue.append(s)
    while len(queue) != 0:
        now = queue.pop()
        if not now in visit:
            visit.append(now)
        for i in d[now]:
            if i in visit:
                continue
            else:
                queue.append(i)
    return visit

def bfs(d, s):
    queue = []
    visit = []
    queue.append(s)
    while len(queue) != 0:
        now = queue.pop(0)
        if now in visit:
            continue
        visit.append(now)
        for i in d[now]:
            queue.append(i)
    return visit    

n, v, s = map(int, sys.stdin.readline().split())

d = {}
for i in range(n):
    d[i+1] = []
for _ in range(v):
    start, end = map(int, sys.stdin.readline().split())
    d[start].append(end)
    d[end].append(start)

for key in d:
    d[key].sort()

d1 = d.copy()
for key in d1:
    d1[key] = sorted(d1[key], reverse=True)
print(*dfs(d1, s))  
  
d2 = d.copy()
print(*bfs(d2, s))    
