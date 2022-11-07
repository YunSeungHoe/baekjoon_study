num = input()
count = 0

def three(n):
    n = list(n)
    sum = 0
    for i in n:
        sum += int(i)
    return str(sum)

while True:
    if int(num) < 10:
        if int(num) % 3 == 0:
            print(count)
            print("YES")
            break
        else:
            print(count)
            print("NO")
            break
    count += 1
    num = three(num)