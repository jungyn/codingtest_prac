import sys
input=sys.stdin.readline

st1 = list(input().rstrip())
st2 = []

n = int(input())
for i in range(n):
    cmd = list(input().split())
    if cmd[0] == 'L':
        if st1:
            st2.append(st1.pop())
    if cmd[0] == 'D':
        if st2:
            st1.append(st2.pop())
    if cmd[0] == 'B':
        if st1:
            st1.pop()
    if cmd[0] == 'P':
        st1.append(cmd[1])

st1.extend(reversed(st2))
print(''.join(st1))