n = int(input())
even = '* '
odd = ' *'
for i in range(n):
    if i % 2 == 0:
        print(even*n)
    else:
        print(odd*n)
        