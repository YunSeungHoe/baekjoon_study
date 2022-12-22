import sys
t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    map_n1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    all_map = [map_n1] * (k+1)
    for i in range(1, k+1):
        for j in range(1, n):
            all_map[i][j] = all_map[i-1][j] + all_map[i][j-1]
    print(all_map[k][n-1])