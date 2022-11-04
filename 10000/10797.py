day = int(input())
car = list(map(int, input().split()))
count = 0
for i in car:
    if i == day:
        count += 1
print(count)