# 이분탐색
n, m = map(int, input().split())
tree = list(map(int, input().split()))

start = 0
end = max(tree)
result = 0

while start <= end:
    mid = (start + end) // 2
    hap = sum(max(0, x - mid) for x in tree)
    
    if hap >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)