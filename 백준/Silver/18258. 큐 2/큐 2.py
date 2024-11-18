# 일반 리스트보다 deque()가 시간이 빠름
import sys
from collections import deque

N = int(sys.stdin.readline())
que = deque()
for _ in range(N):
    cmd = sys.stdin.readline().split()
    if 'push' in cmd:
        que.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
            que.popleft() # deque에서 맨 앞 정수 빼기는 popleft()
    elif cmd[0] == 'size':
        print(len(que))
    elif cmd[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif cmd[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])