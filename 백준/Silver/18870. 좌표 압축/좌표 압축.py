n = int(input())
li = list(map(int, input().split()))

dict = {}
sli = sorted(set(li))

for i, v in enumerate(sli):
    dict[v] = i

for i in li:
    print(dict[i], end=' ')