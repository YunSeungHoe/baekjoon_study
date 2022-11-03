n = int(input())
score = list(input())
anum = 0
bnum = 0
for i in range(n):
    if score[i] == 'A':
        anum += 1
    elif score[i] == 'B':
        bnum += 1
if anum > bnum: print('A')
elif anum < bnum: print('B')
else: print('Tie')
        