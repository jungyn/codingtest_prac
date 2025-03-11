from collections import deque

T = int(input())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque([(x,y)])
    matrix[x][y] = 0

    while queue:
        x, y = queue.popleft()      # 방문 좌표 제거

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if matrix[nx][ny] == 1:
                queue.append((nx, ny))
                matrix[nx][ny] = 0

for _ in range(T):
    m, n, k = map(int, input().split())
    matrix = [[0] * n for _ in range(m)] # 빈 배추밭
    cnt = 0

    for _ in range(k):
        x, y = map(int, input().split())
        matrix[x][y] = 1 # 배추 위치 표시

    for j in range(m):
        for k in range(n):
            if matrix[j][k] == 1:
                bfs(j, k)
                cnt += 1

    print(cnt)