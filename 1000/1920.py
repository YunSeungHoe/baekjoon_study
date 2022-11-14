# binary search 알고리즘 사용
n = int(input())
narr = list(map(int ,input().split()))
m = int(input())
marr = list(map(int ,input().split()))

def binary(arr1, val, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr1[mid] == val:
            return 1
        elif arr1[mid] > val:
            end = mid - 1
        elif arr1[mid] < val:
            start = mid + 1
    return 0
            
narr.sort()

for i in marr:
    print(binary(narr, i, 0, n-1))
