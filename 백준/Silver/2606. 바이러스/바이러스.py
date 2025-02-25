n = int(input())
m = int(input())

graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

visited = [0] * (n+1)

from collections import deque

def bfs(v):
    answer = 0
    queue = deque([v])
    visited[v] = 1

    while queue:
        v = queue.popleft()
        answer += 1
        for i in range(1, n+1):
            if visited[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                visited[i] = 1
    print(answer-1)

bfs(1)