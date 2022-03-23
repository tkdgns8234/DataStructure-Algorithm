# 문제1 그림
from collections import deque

move_type = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(x, y, visited):
    global max_size
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        for move in move_type:
            nx, ny = x + move[0], y + move[1]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))
    if cnt > 0:
        max_size = max(max_size, cnt)
        return True


n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

max_size = 0
count = 0
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            if bfs(i, j, visited):
                count += 1

print(count, max_size, end="\n")