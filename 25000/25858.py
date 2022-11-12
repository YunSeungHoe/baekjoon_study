n, all = map(int, input().split())
people = []
sum = 0
for _ in range(n):
    m = int(input())
    sum += m
    people.append(m)
for i in people:
    print(all * i//sum)