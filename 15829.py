l = int(input())
src = list(input())
# a - 96 = 1
sum = 0
for i in range(l):
    sum += (ord(src[i]) - 96) * pow(31, i)
print(sum%1234567891)