from collections import deque
import sys, copy

NON = 0
EAT = 1
PASS = 2
DONT = 3
NOW = -1

size = 2
exp = 0
n = int(sys.stdin.readline())
space = deque([])
for _ in range(n):
    space.append(deque(list(map(int, sys.stdin.readline().split()))))

while True:
    temp_space = space.copy()
    res = 0
    queue = deque([])
    s = 0
    for i in range(n):
        for j in range(n):
            if space[i][j] == 0:
                temp_space[i][j] = NON
                continue
            res += 1
            if space[i][j] < size:
                temp_space[i][j] = EAT
            elif space[i][j] == size:
                temp_space[i][j] = PASS
            elif space[i][j] < 9:
                temp_space[i][j] = DONT
            elif space[i][j] == 9:
                temp_space[i][j] == NOW
                queue.append((i,j))
    
    if res == 0:
        break
    
    while True:
        cnt = 0
        while len(queue) != 0:
            x, y = queue.popleft()
            if temp_space[x][y] == EAT:
                s += cnt
                break
            temp_queue = deque([])
            if y != 0:
                if temp_space[x][y-1] != DONT:
                    temp_queue.append((x, y-1))
                
            if x != 0:
                if temp_space[x-1][y] != DONT:
                    temp_queue.append((x-1, y))
            if x != n-1:
                if temp_space[x+1][y] != DONT:
                    temp_queue.append((x+1, y))
            if y != n-1:
                if temp_space[x][y+1] != DONT:
                    temp_queue.append((x, y+1))
        if len(temp_queue) == 0:
            break 
        else:           
            queue = temp_queue
            cnt += 1
            temp_queue = deque([])
        아기 상어 뚜루뚜루뚭