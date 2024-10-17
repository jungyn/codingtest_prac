n = int(input())

que = []
for _ in range(n):
    cmd = input()
    if cmd[:4] == 'push':
        que.append(cmd[5:])
    elif cmd == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
            que.pop(0)
    elif cmd == 'size':
        print(len(que))
    elif cmd == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif cmd == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])