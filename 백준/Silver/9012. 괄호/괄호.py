T = int(input())
for i in range(T):
    gh = input()
    stack = []
    is_valid = True
    for j in gh:
        if j == '(':
            stack.append(j)
        else:
            if stack:
                stack.pop()
            else:
                is_valid = False
                break
                
    if is_valid and len(stack) == 0:
        print('YES')
    else:
        print('NO')