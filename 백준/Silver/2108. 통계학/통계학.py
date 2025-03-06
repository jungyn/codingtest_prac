import sys
input=sys.stdin.readline

n = int(input())
su = [int(input()) for _ in range(n)]
su.sort()

# 1. 산술평균
mean = sum(su) / len(su)
mean = round(mean, 0)
print(int(mean))

# 2. 중앙값
idx = int(len(su) / 2)
print(su[idx])

# 3. 최빈값
from collections import Counter
cnt = Counter(su).most_common()
max_cnt = cnt[0][1]
ans = []
for i in range(len(cnt)):
    if cnt[i][1] == max_cnt:
        ans.append(cnt[i][0])
ans.sort()
if len(ans) <= 1:
    print(ans[0])
else:
    print(ans[1])

# 4. 범위
print(su[-1] - su[0])