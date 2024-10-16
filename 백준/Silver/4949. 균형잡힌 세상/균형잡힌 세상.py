import re

while True:
    stc = input()
    if stc == '.':
        break
    stc = re.sub(r'[a-zA-Z0-9]', '', stc)
    stc = stc.replace('.', '')
    gh = stc.replace(' ', '')

    stack = []
    is_valid = True
    for i in gh:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if '(' not in stack or stack[-1] != '(':
                is_valid = False
            else:
                stack.pop()
        elif i == ']':
            if '[' not in stack or stack[-1] != '[':
                is_valid = False
            else:
                stack.pop()

    if not stack and is_valid:
        print('yes')
    else:
        print('no')