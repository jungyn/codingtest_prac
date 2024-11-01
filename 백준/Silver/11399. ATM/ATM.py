n = int(input())
p = list(map(int, input().split()))
p.sort(reverse=True)

answer = 0
for i in range(n, 0, -1):
    answer += p[i-1]*i
print(answer)