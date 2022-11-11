from collections import deque

n, k = map(int, input().split())
cnt = deque([i+1 for i in range(n)])

print("<",end='')
while len(cnt) > 1:
    for _ in range(k-1):
        cnt.append(cnt.popleft())
    print(cnt.popleft(), end='')        
    print(", ",end='')
print(cnt[0], end='')        
print(">")

