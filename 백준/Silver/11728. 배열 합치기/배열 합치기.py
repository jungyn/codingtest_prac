import sys
input = sys.stdin.readline

a, b = map(int, input().split())
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))

alist.extend(blist)
ans = ' '.join(map(str, sorted(alist)))
print(ans)