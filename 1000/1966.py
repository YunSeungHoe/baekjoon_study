import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    paper = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    while len(paper) != 0:
        if max(paper) == paper[0]:
            cnt += 1
            if m == 0:
                break
            else:
                m -= 1
            paper.pop(0)
        else:
            temp = paper.pop(0)
            paper.append(temp)
            m -= 1
            if m < 0:
                m = len(paper) - 1
    print(cnt)