# EOF까지 입력 받기
while True:
    try:
        n = list(map(int, input().split()))
        if n == "":
            break
        print(n[1]//(n[0]+1))
    except:
        break