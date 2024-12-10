n, m = map(int, input().split())

answer = []
for i in range(1, n+1):
    answer.append(i)

for _ in range(m):
    i, j = map(int, input().split())
    answer[i-1], answer[j-1] = answer[j-1], answer[i-1]

for ans in answer:
    print(ans, end=' ')