bowl = list(input())
h = 10
temp = bowl[0]
for i in bowl[1:]:
    if temp == i:
        h += 5
    else:
        temp = i
        h += 10
print(h)