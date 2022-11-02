size = int(input())
        
def gcd(a, b):  # 최대공약수
    while b > 0:
        a, b = b, a % b
    return a

for i in range(size):
    a, b = map(int, input().split())
    print(int(a*b/gcd(a, b)))