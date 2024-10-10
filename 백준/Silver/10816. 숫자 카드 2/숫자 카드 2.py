from collections import Counter

n = int(input())
nlist = sorted(map(int, input().split()))
m = int(input())
mlist = map(int, input().split())

count_dict = Counter(nlist)

for i in mlist:
    print(count_dict[i], end=' ')