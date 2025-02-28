n = int(input())
card = [int(input()) for _ in range(n)]
ans = []

from collections import Counter
cnt = Counter(card).most_common() # 데이터 개수 많은 순대로

max_cnt = cnt[0][1]
for i in cnt:
    if i[1] == max_cnt:
        ans.append(i[0])
ans.sort()
print(ans[0])