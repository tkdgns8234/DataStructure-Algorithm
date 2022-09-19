from itertools import combinations
from collections import deque
from copy import deepcopy

N, M = map(int, input().split())

virus = []
wall = []
none = []

NONE = 0
WALL = 1
VIRUS = 2

data = []
for i in range(N):
    temp = list(map(int, input().split()))
    for j, t in enumerate(temp):
        if t == NONE:
            none.append((i, j))
        if t == WALL:
            wall.append((i, j))
        if t == VIRUS:
            virus.append((i, j))
    data.append(temp)


move_type = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# 3개의 벽 설치하는 모든 경우의 수
def bfs(start, temp_data):
    visited[start[0]][start[1]] = True
    virus_cnt = 1

    q = deque([start])
    while q:
        x, y = q.popleft()
        for move in move_type:
            nx = x + move[0]
            ny = y + move[1]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and temp_data[nx][ny] == NONE:
                    # 바이러스 퍼뜨리기
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    virus_cnt += 1

    return virus_cnt


result = -int(1e9)
for comb in combinations(none, 3):

    temp_data = deepcopy(data)
    # 벽 설치
    for x, y in comb:
        temp_data[x][y] = WALL

    visited = [[False] * M for _ in range(N)]
    v_sum = 0
    for v in virus:
        v_sum += bfs(v, temp_data)

    result = max(result, N*M - len(wall) - v_sum - 3)

print(result)
