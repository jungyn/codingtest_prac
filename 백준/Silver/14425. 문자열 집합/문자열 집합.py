n, m = map(int, input().split())
answer = 0
string = []

for _ in range(n):
    nlist = input()
    string.append(nlist)
for _ in range(m):
    mlist = input()
    if mlist in string:
        answer += 1

print(answer)