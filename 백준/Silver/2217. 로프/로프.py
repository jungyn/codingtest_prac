n = int(input())
wlist = []

for _ in range(n):
    w = int(input())
    wlist.append(w)
wlist.sort(reverse=True)

answer = 0
for i in range(n):
    answer = max(answer, wlist[i]*(i+1))
print(answer)