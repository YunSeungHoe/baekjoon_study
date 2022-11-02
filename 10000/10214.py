n = int(input())
Ysum = 0
Ksum = 0
for i in range(n):
    for j in range(9):
        y, k = map(int, input().split())
        Ysum += y
        Ksum += k
    if Ysum > Ksum:
        print("Yonsei")
    elif Ysum < Ksum:
        print("Korea")
    else:
        print("Draw")
    Ysum = 0
    Ksum = 0