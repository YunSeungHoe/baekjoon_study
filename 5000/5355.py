n = int(input())
for x in range(n):
    command = list(input().split())
    num = float(command[0])
    for i in command[1:]:
        if i == '@':
            num = num * 3
        elif i == '%':
            num += 5
        elif i == '#':
            num -= 7
            
    print("{0:.2f}".format(num))
    