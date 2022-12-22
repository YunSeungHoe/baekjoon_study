m, n = map(int, input().split())
trees = list(map(int, input().split()))

s = 0
e = max(trees) - 1

while True:
    if s > e:
        break
    mid = (s+e)//2
    sum = 0
    for i in trees:
        if i - mid > 0:
            sum += i - mid
    if sum > n:
        s = mid + 1
    elif sum < n:
        e = mid - 1
    else:
        break
if sum >= n:
    print(mid)
else:
    print(e)