sec = int(input())
a = 300
b = 60
c = 10

if sec >= a:
    a = int(sec/a)
    sec -= a * 300
else:
    a = 0
if sec >= b:
    b = int(sec/b)
    sec -= b * 60
else: 
    b = 0
    
if sec >= c:
    c = int(sec/c)
    sec -= c * 10
else:
    c = 0

if sec == 0:
    print(a, b, c)
else:
    print(-1)