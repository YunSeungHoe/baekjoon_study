l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

k = a//c
if a%c != 0:
    k += 1
e = b//d
if b%d != 0:
    e += 1
if k >= e:
    print(l-k)
else:
    print(l-e)