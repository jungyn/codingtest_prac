n, m = map(int, input().split())

answer = [x for x in range(1, n+1)]
for _ in range(m):
    i, j = map(int, input().split())    
    rev = answer[i-1:j][::-1]
    answer[i-1:j] = rev
for ans in answer:
    print(ans, end=' ')