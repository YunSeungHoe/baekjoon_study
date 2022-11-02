student= [0, 0, 0, 0, 0,
          0, 0, 0, 0, 0,
          0, 0, 0, 0, 0,
          0, 0, 0, 0, 0,
          0, 0, 0, 0, 0,
          0, 0, 0, 0, 0]
for i in range(28):
    n = int(input())
    student[n-1] += 1

for i in range(30):
    if student[i] == 0:
        print(i+1)
    