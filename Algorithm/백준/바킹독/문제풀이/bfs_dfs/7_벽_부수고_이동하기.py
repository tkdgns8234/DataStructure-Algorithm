# 7. 벽 부수고 이동하기
# 풀이가 쉽게 떠오르지 않아 블로그를 참조했다
# 3차원 형식의 bfs 문제였다
# bfs, dfs는 완전탐색알고리즘의 일종이다
# 따라서 모든곳을 탐색하게 되고, 벽을 한번만 뚫도록 구현하는것도 3차원 배열을 이용하면 가능하다
# 아주 좋은 문제였다

import sys
from collections import deque
input = sys.stdin.readline
move_type = [(-1,0),(1,0),(0,1),(0,-1)]
n, m = map(int, input().rstrip().split())
data = []
for i in range(n):
    temp = list(map(int, list(input().rstrip())))
    data.append(temp)
dist = [[[0] * 2 for i in range(m)] for _ in range(n)]  # 벽돌 부순것과 부수지 않은것

q = deque()
q.append((0, 0, 0)) # 0 = wall 을 깨지않은상태 1 = 깬 상태
dist[0][0][0] = 1
while q:
    x, y, wall = q.popleft()
    if x == n-1 and y == m-1:
        print(dist[x][y][wall])
        exit(0)
    for move in move_type:
        nx, ny = x + move[0], y + move[1]
        if 0 <= nx < n and 0 <= ny < m and dist[nx][ny][wall] == 0:
            if data[nx][ny] == 1:  # 벽인 경우
                if wall == 0: # 벽돌을 깬적이 없는 경우
                    q.append((nx,ny,1))  # 1 은 벽돌을 깬 경우로 표시, 이동
                    dist[nx][ny][1] = dist[x][y][wall] + 1
            else:
                q.append((nx,ny,wall))
                dist[nx][ny][wall] = dist[x][y][wall] + 1
print(-1)