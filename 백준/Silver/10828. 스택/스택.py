n = int(input())

stack = []

for _ in range(n):
    cmd = input()
    if cmd[:4] == 'push':
        stack.append(cmd[5:])
    elif cmd == 'pop':
        if stack == []:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        if stack == []:
            print(1)
        else:
            print(0)
    elif cmd == 'top':
        if stack == []:
            print(-1)
        else:
            print(stack[-1])