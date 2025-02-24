n, k = map(int, input().split())
score = list(map(int, input().split()))
score = sorted(score)[::-1]
print(score[k-1])