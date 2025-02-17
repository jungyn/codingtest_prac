n, m, v = map(int, input().split())

# 행렬 만들기
graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1       # 정점이 연결되어 있으면 1

# 방문 리스트 만들기
visited1 = [0] * (n+1)       # dfs
visited2 = [0] * (n+1)       # bfs

def dfs(v):
    visited1[v] = 1      # 시작 노드 방문 표시
    print(v, end=' ')
    for i in range(1, n+1):
        if graph[v][i] == 1 and visited1[i] == 0: # 노드가 연결되어 있고 방문한 적이 없다
            dfs(i)

dfs(v)
print() # 들여쓰기

def bfs(v):
    queue = [v]
    visited2[v] = 1
    while queue:
        v = queue.pop(0)    # 방문 노드 제거
        print(v, end=' ')
        for i in range(1, n+1):
            if graph[v][i] == 1 and visited2[i] == 0:
                queue.append(i)    # 큐에 i를 삽입
                visited2[i] = 1    # 방문처리
bfs(v)