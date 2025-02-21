import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0] * (n+1)

for p in range(1, n+1):
    prefix[p] = arr[p-1] + prefix[p-1]

for _ in range(m):
    i, j = map(int, input().split())
    print(prefix[j] - prefix[i-1])