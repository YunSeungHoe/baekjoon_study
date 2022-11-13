ham = []
drink = []
for _ in range(3):
    ham.append(int(input()))
for _ in range(2):
    drink.append(int(input()))
print(min(ham) + min(drink) - 50)