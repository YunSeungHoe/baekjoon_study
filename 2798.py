def black(n, m, arr):
    sum = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                sum = arr[i] + arr[j] + arr[k]
                if sum == m:
                    print(m)
                    return 
n, m = map(int, input().split())
arr = list(map(int, input().split()))
sum = 0
arr.sort()
black(n, m, arr)