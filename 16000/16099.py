n = int(input())
for _ in range(n):
    lt, wt, le, we = map(int, input().split())
    if lt*wt > le*we:
        print("TelecomParisTech")
    elif lt*wt == le*we:
        print("Tie")
    else: print("Eurecom")