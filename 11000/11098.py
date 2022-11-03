n = int(input())
for i in range(n):
    max = 0
    player = int(input())
    for j in range(player):
        pri, name = input().split()
        if max < int(pri):
            max = int(pri)
            max_name = name
    print(max_name)