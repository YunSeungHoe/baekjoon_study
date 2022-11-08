n = int(input())
count = 0
six = 666
while(True):
    if '666' in str(six):
        count += 1
    if count == n:
        break
    six += 1
print(six)