from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    while fire_q:
        x, y = fire_q.popleft()
        for move in move_type:
            nx, ny = x+move[0], y+move[1]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if data[nx][ny] == '#' or dist_fire[nx][ny] > 0:
                continue
            dist_fire[nx][ny] = dist_fire[x][y] + 1
            fire_q.append((nx,ny))

    while jh_q:
        x, y = jh_q.popleft()
        for move in move_type:
            nx, ny = x+move[0], y+move[1]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                return dist_jh[x][y] + 1
            if data[nx][ny] == '#' or dist_jh[nx][ny] > 0:
                continue
            if dist_fire[nx][ny] == 0 or dist_fire[nx][ny] > dist_jh[x][y] + 1:
                jh_q.append((nx,ny))
                dist_jh[nx][ny] = dist_jh[x][y] + 1
    return 'IMPOSSIBLE'

move_type = [(-1, 0),(1, 0),(0, 1),(0, -1)]

n, m = map(int, input().split())
jh_q, fire_q = deque(), deque()
dist_jh, dist_fire = [[0]*m for i in range(m)], [[0]*m for i in range(m)]
data = []
for i in range(n):
    temp = list(input().rstrip())
    data.append(temp)
    for j in range(len(temp)):
        if temp[j] == 'J':
            jh_q.append((i,j))
        elif temp[j] == 'F':
            fire_q.append((i,j))

print(bfs())

