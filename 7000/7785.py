n = int(input())
people = dict()
for _ in range(n):
    name, state = input().split()
    if state == "enter":
        people[name] = 1
    else:
        del people[name]

for i in sorted(people.keys(), reverse=True):
    print(i)