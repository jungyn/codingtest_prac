n = int(input())
score = list(map(int, input().split()))

ms = max(score)
mean = []
for i in score:
    temp = i/ms * 100
    mean.append(temp)
print(sum(mean)/len(mean))