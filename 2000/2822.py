val = []
index = []
for _ in range(8):
    val.append(int(input()))

temp = val.copy()
val = sorted(val)
print(sum(val[3:]))

for i in val[3:]:
    index.append(temp.index(i)+1)

print(*sorted(index))