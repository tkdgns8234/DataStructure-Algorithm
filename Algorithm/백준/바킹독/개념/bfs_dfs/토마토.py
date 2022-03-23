
# 문제3 토마토
from collections import deque
m, n = map(int, input().split())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            q.append((i, j))
            visited[i][j] = True

move_type = [(-1, 0), (1, 0), (0, 1), (0, -1)]
while q:
    x, y = q.popleft()
    for move in move_type:
        nx, ny = x + move[0], y + move[1]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if data[nx][ny] == 0 and not visited[nx][ny]:
            visited[nx][ny] = True
            q.append((nx, ny))
            data[nx][ny] = data[x][y] + 1


for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            print(-1)
            exit(0)
print(max(map(max, data)) - 1)
