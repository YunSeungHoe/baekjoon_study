MaxScore = 0
MaxPeople = 0
for i in range(5):
    score = list(map(int, input().split()))
    PeopleScore = sum(score)
    if PeopleScore > MaxScore:
        MaxScore = PeopleScore
        MaxPeople = i + 1
print(MaxPeople, MaxScore)