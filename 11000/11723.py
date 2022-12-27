import sys
n = int(sys.stdin.readline())
set1 = set()
for _ in range(n):
    cmd = sys.stdin.readline().split()
    if len(cmd) == 1:
        if cmd[0] == 'all':
            set1 = {i for i in range(1, 21, 1)}
        elif cmd[0] == 'empty':
            set1 = set()
    elif len(cmd) == 2:
        if cmd[0] == 'add':
            if int(cmd[1]) in set1:
                continue
            set1.add(int(cmd[1]))
        elif cmd[0] == 'remove':
            if not int(cmd[1]) in set1:
                continue
            set1.remove(int(cmd[1]))
        elif cmd[0] == 'check':
            if int(cmd[1]) in set1:
                print('1')
            else: 
                print('0')
        elif cmd[0] == 'toggle':
            if int(cmd[1]) in set1:
                set1.remove(int(cmd[1]))
            else:
                set1.add(int(cmd[1]))
