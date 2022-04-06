# 1. 유기농 배추
from collections import deque
move_type = [(-1, 0), (1, 0), (0, -1), (0, 1)]

T = int(input())

def bfs(x, y):
    visited[x][y] = True
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for move in move_type:
            nx, ny = x + move[0], y + move[1]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if not visited[nx][ny] and data[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))
    return

for _ in range(T):
    count = 0
    n, m, k = map(int, input().split())
    data = [[0] * m for i in range(n)]

    for i in range(k):
        x, y = map(int, input().split())
        data[x][y] = 1

    visited = [[False] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and data[i][j] == 1:
                bfs(i, j)
                count += 1
    print(count)