while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    f1 = False
    f2 = False    
    if a > b:
        for i in range(1, a+1):
            if a/i == b:
                print("multiple")
                f1 = True
                break
    else:
        for i in range(1, b+1):
            if b/i == a:
                print("factor")
                f2 = True
                break
    if f1 == False and f2 == False:
        print("neither")