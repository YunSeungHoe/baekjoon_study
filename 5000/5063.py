n = int(input())
for i in range(n):
    r, e, c = map(int, input().split())
    no = r + c
    if no > e:
        print("do not advertise")
    elif no == e:
        print("does not matter")
    else:
        print("advertise")