x = list(map(int, input().split()))
for i in range(1, len(x)-1):
    if abs(x[i-1] - x[i]) != 1:
        print("mixed")
        exit(0)
if x[0] == 1: print("ascending")
else: print("descending")