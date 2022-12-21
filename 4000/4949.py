import sys

while True:
    que = []
    cmd = sys.stdin.readline().strip('\n')
    if cmd == "." and len(cmd) == 1:
        break
    for i in cmd:
        if i =='.': 
            break
        elif i == '(' or i == '[':
            que.append(i)
        elif i == ']':
            if len(que) != 0 and que[-1] == '[':
                que.pop()
            else: 
                que.append(i)
        elif i == ')':
            if len(que) != 0 and que[-1] == '(':
                que.pop()
            else: 
                que.append(i)
    if(len(que)) == 0:
        print('yes')
    else: print('no')