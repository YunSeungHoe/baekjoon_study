from collections import Counter
val = []
for i in range(10):
    num = int(input())
    val.append(num)
cnt = Counter(val)

print(int(sum(val)/10))
print(cnt.most_common(1)[0][0])