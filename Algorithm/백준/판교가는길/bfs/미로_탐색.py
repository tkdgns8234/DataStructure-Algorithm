from collections import deque
n, m = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, str(input()))))

visited = [[False] * m for _ in range(n)]

q = deque()
q.append((0, 0))
visited[0][0] = True

move_type = [(-1, 0), (1, 0), (0, 1), (0, -1)]
while q:
    x, y = q.popleft()
    for move in move_type:
        nx, ny = move[0] + x, move[1] + y
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if not visited[nx][ny] and data[nx][ny] == 1:
            visited[nx][ny] = True
            q.append((nx, ny))
            data[nx][ny] = data[x][y] + 1

print(data[n-1][m-1])