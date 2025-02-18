# 런타임에러

from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001

def bfs():
    q = deque()
    q.append(n)
    
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        for j in (x-1, x+1, 2*x):
            if 0 <= j <= 100000 and not visited[j]:
                visited[j] = visited[x] + 1
                q.append(j)

bfs()