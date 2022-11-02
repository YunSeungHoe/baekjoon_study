n = int(input())
command = list(map(int, input().split()))
x = int(input())
count = 0

for i in command:
    if x == i:
        count += 1 

print(count)