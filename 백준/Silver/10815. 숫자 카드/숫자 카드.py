n = int(input())
nlist = set(map(int, input().split())) # 시간초과 : list -> set
m = int(input())
mlist = list(map(int, input().split()))

dict = {}
for ans in mlist:
    dict[ans] = 0

for i in nlist:
    if i in dict:
        dict[i] = 1

for d in dict:
    print(dict[d], end=' ')