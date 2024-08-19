n = int(input())
lst = []
for _ in range(n):
    su = int(input())
    lst.append(su)
lst.sort()
for i in lst:
    print(i)