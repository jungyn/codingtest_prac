N = int(input())
A = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))
A.sort()

# 이진탐색
def binary_search(array, target):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for li in arr:
    if binary_search(A, li) == None:
        print(0)
    else:
        print(1)