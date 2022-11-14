n = int(input())
print("Gnomes:")
for _ in range(n):
    arr = list(map(int, input().split()))
    if arr[0] == min(arr) and arr[2] == max(arr):
        print("Ordered")
    elif arr[0] == max(arr) and arr[2] == min(arr):
        print("Ordered")
    else:
        print("Unordered")
        