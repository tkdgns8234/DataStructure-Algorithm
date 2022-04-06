# 문제 12 말이 되고픈 원숭이
# 벽돌 부수기와 매우 유사해보여 말처럼 이동한 횟수를 3차원배열 위치에 표시하도록 해보자
import sys
from collections import deque
input = sys.stdin.readline

move_type = [(-1, 0), (1, 0), (0, 1), (0, -1)]
horse_move_type = [(-1, -2), (-2, -1), (-2, 1), (-1, 2),
      (1, -2), (2, -1), (2, 1), (1, 2)]

k = int(input())
m, n = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dist = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]
dist[0][0][0] = 1

q = deque()
q.append((0,0,0))

while q:
    x, y, horse = q.popleft()
    if x == n-1 and y == m-1:
        print(dist[x][y][horse]-1)
        exit(0)
    for move in move_type:
        nx, ny = x + move[0], y + move[1]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if data[nx][ny] == 0 and dist[nx][ny][horse] == 0:
            dist[nx][ny][horse] = dist[x][y][horse] + 1
            q.append((nx, ny, horse))
    if horse < k:
        for move in horse_move_type:
            nx, ny = x + move[0], y + move[1]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if data[nx][ny] == 0 and dist[nx][ny][horse+1] == 0:
                dist[nx][ny][horse+1] = dist[x][y][horse] + 1
                q.append((nx, ny, horse+1))

print(-1)