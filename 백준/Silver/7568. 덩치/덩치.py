n = int(input())

data = []
rank = []

for i in range(n):
    x, y = map(int, input().split())
    data.append((x, y))

for i in range(n):
    count = 0
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            count += 1
    rank.append(count+1)

for r in rank:
    print(r, end=' ')