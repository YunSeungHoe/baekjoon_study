n = int(input())
cute = 0
for i in range(n):
    ans = int(input())
    if ans == 0:
        cute -= 1
    else: cute += 1
if cute > 0: print("Junhee is cute!")
else: print("Junhee is not cute!")