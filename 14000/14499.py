EAST = 1
WEST = 2
NORTH = 3
SOUTH = 4

n, m, x, y, k = map(int, input().split())
grid = []
command = []
dice = [0, 0, 0, 0, 0, 0]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def tumble(val):
    if val == EAST:
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]
    elif val == WEST:
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
    elif val == NORTH:
        dice[1], dice[5], dice[3], dice[4] = dice[5], dice[3], dice[4], dice[1]
    elif val == SOUTH:
        dice[1], dice[5], dice[3], dice[4] = dice[4], dice[1], dice[5], dice[3]

for i in range(n):
    grid.append(list(map(int, input().split())))

command = list(map(int, input().split()))
nx, ny = x, y
for i in command:
    nx += dx[i-1]
    ny += dy[i-1]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        nx -= dx[i-1]
        ny -= dy[i-1]
        continue
    tumble(i)
    if grid[nx][ny] == 0:
        grid[nx][ny] = dice[1]
    else:
        dice[1] = grid[nx][ny] 
        grid[nx][ny] = 0
    print(dice[3])