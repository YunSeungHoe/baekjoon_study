while True:
    people = list(input().split())
    if people[0] == '#' and people[1] == '0' and people[2] == '0':
        break
    if int(people[1]) > 17 or int(people[2]) >= 80:
        print(people[0], "Senior")
    else:
        print(people[0], "Junior")