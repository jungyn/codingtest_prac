n, m = map(int, input().split())

dict = {}
for i in range(1, n+1):
    pk = input()
    dict[i] = pk
    dict[pk] = i

for q in range(m):
    que = input()

    if que.isdigit():
        print(dict[int(que)])
    else:
        print(dict[que])