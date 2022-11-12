n = int(input())
for _ in range(n):
    num = list(map(int, input().split()))
    cnt = 0
    for i in num:
        if i >= 10:
            cnt += 1
    print(*num)
    if cnt == 0: print("zilch")
    elif cnt == 1: print("double")
    elif cnt == 2: print("double-double")
    else: print("triple-double")
    print("")