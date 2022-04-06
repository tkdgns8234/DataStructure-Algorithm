# 6. 불
from collections import deque
import sys
input = sys.stdin.readline

move_type = [(-1,0),(1,0),(0,1),(0,-1)]
def bfs():
    while fire_q:
        x, y = fire_q.popleft()
        for move in move_type:
            nx, ny = move[0] + x, move[1] + y
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if data[nx][ny] != '#' and data[nx][ny] != '*' and fire_dist[nx][ny] == 0:
                fire_dist[nx][ny] = fire_dist[x][y] + 1
                fire_q.append((nx, ny))

    while sg_q:
        x, y = sg_q.popleft()
        for move in move_type:
            nx, ny = move[0] + x, move[1] + y
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                return sg_dist[x][y] + 1
            if sg_dist[nx][ny] > 0 or data[nx][ny] == '#' or data[nx][ny] == '*' or data[nx][ny] == '@':
                continue
            if fire_dist[nx][ny] == 0 or fire_dist[nx][ny] > sg_dist[x][y] + 1:
                sg_dist[nx][ny] = sg_dist[x][y] + 1
                sg_q.append((nx,ny))
    return 'IMPOSSIBLE'


T = int(input().rstrip())
for _ in range(T):
    m, n = map(int, input().rstrip().split()) #n x m y
    sg_q, fire_q = deque(), deque()
    sg_dist, fire_dist = [[0] * m for i in range(n)], [[0] * m for i in range(n)]
    data = []

    for i in range(n):
        temp = list(input().rstrip())
        data.append(temp)
        for j in range(len(temp)):
            if temp[j] == '@':
                sg_q.append((i,j))
            elif temp[j] == '*':
                fire_q.append((i,j))

    print(bfs())