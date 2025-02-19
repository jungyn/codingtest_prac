from collections import deque

n, m = map(int, input().split())
lines = [list(map(int, input().strip())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x,y):
    queue = deque([(x,y)])
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if lines[nx][ny] == 0:
                continue
            if lines[nx][ny] == 1:
                lines[nx][ny] = lines[x][y] + 1
                queue.append((nx,ny))
    return lines[n-1][m-1]

print(bfs(0,0))