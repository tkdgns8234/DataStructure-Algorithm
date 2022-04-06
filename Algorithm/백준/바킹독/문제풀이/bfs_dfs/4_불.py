# 4. 불!
# 어떻게 짤지 재대로 구조를 잡지 않고 짜서 코드가 참 길고 가독성이 떨어졌다
# 백준에 제출했던 코드를 보면 알 수 있다
# 1. 일단 visited 변수를 습관적으로 두는데, 이것도 두지 않아도 될 때가 많다
# 2. 정해진 틀에서 벗어나라. 불 또는 지훈 좌표를 바로 q에 넣어도 된다
# (불이 여러개가 될 수 있다는건 지문을 대충읽어서 놓치고있었다)

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