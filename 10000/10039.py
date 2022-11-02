student = []
sum = 0
for i in range(5):
    student.append(int(input()))

for i in student:
    if i < 40:
        sum += 40
    else:
        sum += i
print(int(sum / 5))