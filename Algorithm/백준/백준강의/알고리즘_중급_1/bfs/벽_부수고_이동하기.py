# 이미 푼 문제 해결 방법만 짚고 넘어가기
# 벽을 부순경우와 부수지 않은 경우로 나누어서 풀이


# 이전 풀이
# 문제의 key point
# 1. 돌을 부순 경우와 안부순 경우로 나누는 방법
# 2. bfs 이므로 먼저 방문한곳이 제일 빠름 (dist의 값이 0인경우만 밟도록 구현)
# 2-1. visit을 방문한 거리로 처리
# 3. 시간복잡도 1000*1000*2

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