# 9. 빙산
# 얼음을 녹인 후 bfs로 탐색하자
# 시간이 2000ms가 소요된다
# 짧게는 800ms 까지 가능한것같은데
# 다시풀자
# 좀 더 효율적인 bfs 방법이 분명 있어보여
# 개선을 거친 코드

from collections import deque
import sys
input = sys.stdin.readline  # 개선포인트 0
move_type = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def ice_to_water():
    melt = []  # 개선포인트 1 기존엔 temp 배열을가지고 딥카피 하는식으로 했었음, 비효율적이었음
    for x in range(n):
        for y in range(m):
            water_cnt = 0
            if data[x][y] != 0:
                for move in move_type:
                    nx, ny = x + move[0], y + move[1]
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    if data[nx][ny] == 0:
                        water_cnt += 1
                    melt.append((x, y,  max(0, data[x][y] - water_cnt))) #최솟값은 0
    for a, b, c in melt:
        data[a][b] = c

def bfs():
    cnt = 0
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and data[i][j] != 0:
                cnt += 1
                visited[i][j] = True
                q = deque()
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    for move in move_type:
                        nx, ny = x + move[0], y + move[1]
                        if nx < 0 or ny < 0 or nx >= n or ny >= m:
                            continue
                        if data[nx][ny] > 0 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
    return cnt


n, m = map(int, input().split())
data = [list(map(int, input().split())) for i in range(n)]
passed = 0
while True: # 개선포인트 2 while 문을 조금 더 단순화, 함수안에서 필요한것들을 모두 처리, 중복 for문등 다 함수 안으로
    cnt = bfs()
    if cnt >= 2:
        print(passed)
        break
    elif cnt == 0:
        print(0)
        break

    ice_to_water()
    passed += 1


# 훨씬 더 좋아보이는 코드
# count 라는 변수를 둬서 주변의 water count를 센다.
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

check = False
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    count[x][y] += 1
                elif graph[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny])
    return 1


year = 0
while True:
    visited = [[False] * m for _ in range(n)]
    count = [[0] * m for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visited[i][j]:
                visited[i][j] = True
                result.append(bfs(i, j))

    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                graph[i][j] -= count[i][j]
                if graph[i][j] < 0:
                    graph[i][j] = 0

    if len(result) == 0:
        break
    if len(result) >= 2:
        check = True
        break
    year += 1

if check:
    print(year)
else:
    print(0)