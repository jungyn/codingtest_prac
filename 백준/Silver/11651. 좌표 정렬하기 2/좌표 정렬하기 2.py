n = int(input())

list = []
for _ in range(n):
    x, y = map(int, input().split())
    list.append((x,y))

list.sort(key=lambda x:(x[1], x[0]))
for li in list:
    print(li[0], li[1])