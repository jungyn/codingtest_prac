k = int(input())
su = []
for _ in range(k):
    stack = int(input())
    if stack == 0:
        su.pop()
    else:
        su.append(stack)
print(sum(su))