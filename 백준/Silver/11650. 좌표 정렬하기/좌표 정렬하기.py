n = int(input())
list = []
for _ in range(n):
    x, y = map(int, input().split())
    list.append((x, y))

list.sort(key = lambda x: (x[0], x[1]))
for li in list:
    print(li[0], li[1])