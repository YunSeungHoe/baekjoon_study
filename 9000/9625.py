n = int(input())
a = 1
b = 0
for _ in range(n):
    b, a = a+b, b
print(a, b)
    