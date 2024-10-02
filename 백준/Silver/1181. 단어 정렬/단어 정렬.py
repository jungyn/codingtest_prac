n = int(input())
wlist = []
for _ in range(n):
    word = input()
    wlist.append(word)
wlist = list(set(wlist))
wlist.sort(key=lambda x: (len(x), x)) # 길이 먼저, 그다음 사전 순

for i in wlist:
    print(i)