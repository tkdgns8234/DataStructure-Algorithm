# 10. 연구소
# 3개를 설치하는 모든 경우의 수
# 바이러스 위치 저장, bfs
# 최대 8*8
# 시간복잡도: (64C3) * (nm) bfs
# 정~~~말 잘했다 시간소요 300ms 인데 랭킹 29등이야!!
# 백트래킹으로도 3개를 설치하는 모든 경우의수 계산이 가능하네
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
empty = [] # 빈칸 위치 저장
wall_cnt = 3 # 3개 추가되기 때문
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