# 2. 적록색약
from collections import deque
n = int(input())
data = [[0] * n for _ in range(n)]
data_red_green = [[0] * n for _ in range(n)]
for i in range(n):
    row = list(input())
    for j in range(len(row)):
        data[i][j] = row[j]
        if row[j] == 'G':
            data_red_green[i][j] = 'R'
        else:
            data_red_green[i][j] = row[j]

move_type = [(-1,0),(1,0),(0,1),(0,-1)]
def dfs(x, y, arr):
    global visited
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    chr = arr[x][y]

    while q:
        x, y = q.popleft()
        for move in move_type:
            nx, ny = x + move[0], y + move[1]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if not visited[nx][ny] and arr[nx][ny] == chr:
                visited[nx][ny] = True
                q.append((nx, ny))


for mode in range(2):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if mode == 0:
                    dfs(i, j, data)
                else:
                    dfs(i, j, data_red_green)
                cnt += 1
    print(cnt, end=" ")