n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    print("You get {} piece(s) and your dad gets {} piece(s).".format(x//y, x%y))