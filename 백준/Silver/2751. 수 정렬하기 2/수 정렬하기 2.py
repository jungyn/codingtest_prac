import sys

n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    su = int(sys.stdin.readline())
    lst.append(su)
lst.sort()
for i in lst:
    print(i)