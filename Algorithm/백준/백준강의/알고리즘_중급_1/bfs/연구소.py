# 이미 푼 문제
# 64c3 에 벽을 세우고
# 차례대로 bfs 진행
# 이미 푼 문제

# 이전 풀이
from itertools import combinations
import sys
from collections import deque

input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().split())
visited = [[0] * m for _ in range(n)]
visited_num = 0
data = []  # 0 빈칸, 1 벽, 2 바이러스
virus = []
empty = []
wall_cnt = 3
for i in range(n):
    row = list(map(int, input().rstrip().split()))
    for j in range(len(row)):
        if row[j] == 2:
            virus.append((i, j))
        elif row[j] == 0:
            empty.append(m * i + j)  # 빈칸의 위치는 0 ~ nm 형태로 나타냄
        else:
            wall_cnt += 1
    data.append(row)

move_type = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs():
    global visited_num, max_val
    visited_num += 1
    q = deque(virus)
    count = len(virus)

    while q:
        x, y = q.popleft()
        for move in move_type:
            nx, ny = x + move[0], y + move[1]
            if point_validator(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = visited_num
                count += 1
    max_val = max(max_val, n * m - count - wall_cnt)


def point_validator(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if visited[x][y] == visited_num or data[x][y] != 0:
        return False
    return True


max_val = 0
# 빈칸에서 벽 3개를 설치하는 모든 경우의 수
for case in combinations(empty, 3):
    for c in case:
        data[c // m][c % m] = 1
    bfs()
    for c in case:
        data[c // m][c % m] = 0

print(max_val)

