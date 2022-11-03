n = int(input())
max = [0, 0, 2011]
min = [12, 31, 1989]
for i in range(n):
    name, d, m, y = input().split()
    d, m, y = int(d), int(m), int(y)
    temp = []
    temp.append(d)
    temp.append(m)
    temp.append(y)
    if temp[2] < max[2]:
        max[2] = temp[2]
        max[1] = temp[1]
        max[0] = temp[0]
        who = name
    elif temp[2] == max[2]:
        if temp[1] < max[1]:
            max[1] = temp[1]
            max[0] = temp[0]
            who = name
        elif temp[1] == max[1]:
            if temp[0] < max[0]:
                max[0] = temp[0]
                who = name
    if temp[2] > min[2]:
        min[2] = temp[2]
        min[1] = temp[1]
        min[0] = temp[0]
        mwho = name
    elif temp[2] == min[2]:
        if temp[1] > max[1]:
            min[1] = temp[1]
            min[0] = temp[0]
            mwho = name
        elif temp[1] == min[1]:
            if temp[0] > min[0]:
                min[0] = temp[0]
                mwho = name
print(mwho)
print(who)
                