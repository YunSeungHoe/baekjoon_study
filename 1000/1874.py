import sys
n = int(sys.stdin.readline())
res = []
start = []
stack = []
ret = []
flag = False
cnt = 0

for i in range(n):
    res.append(int(sys.stdin.readline()))
    start.append(i+1)


while True:
    if len(start) == 0 and len(stack) == 0:
        flag = True
        break
    if len(stack) == 0:
        ret.append('+')
        temp = start.pop(0)
        stack.append(temp)
    elif len(start) == 0:
        ret.append('-')
        temp = stack.pop()
        if temp == res[cnt]:
            cnt += 1
        else:
            break
    elif stack[-1] == res[cnt]:
        ret.append('-')
        stack.pop()
        cnt += 1
    else:
        ret.append('+')
        temp = start.pop(0)
        stack.append(temp)
if flag:
    for i in ret:
        print(i)
else:
    print('NO')