size = int(input())
for i in range(size):
    max = 0
    n = int(input())
    for j in range(n):
        school, num = input().split()
        if max < int(num):
            max = int(num)
            maxschool = school
    print(maxschool)