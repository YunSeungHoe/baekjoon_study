string = list(input())
temp = string.copy()
string.reverse()
flag = True
for i in range(len(string)):
    if string[i] != temp[i]:
        flag = False
if flag == True: print(1)
else: print(0)