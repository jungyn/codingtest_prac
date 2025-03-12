import sys
input=sys.stdin.readline

n = int(input())
stack = []
ans = []
now = 1
find = True

for i in range(n):
    su = int(input())
    while now <= su:
        stack.append(now)
        ans.append('+')
        now += 1
    if stack[-1] == su:
        stack.pop()
        ans.append('-')
    else:
        find = False

if not find:
    print('NO')
else:
    print(' '.join(ans))