def Rev(n):
    n = list(str(n))
    n.reverse()
    n = int(''.join(n))
    return n        
    
a, b = map(int, input().split())
print(Rev(Rev(a) + Rev(b)))