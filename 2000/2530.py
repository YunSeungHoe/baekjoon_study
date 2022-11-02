h, m, s = map(int, input().split())
x = int(input())

sum = 3600 * h + 60 * m + s + x

h = sum // 3600
if h >= 24:
    h = h % 24

sum = sum % 3600
m = sum // 60
if m >= 60:
    m = m % 60

s = sum % 60

print(h, m, s)