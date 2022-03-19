# 1. 입력받은 섬을 각각 다른 숫자로 변경
# 2. 0이 아닌 경우 bfs 로 탐색, 바다를 건넌 count를 q에 같이 넘기기
# 3. 다른 섬에 도착한 경우 멈추고 최소 count 계속 찾기
from collections import deque

move_type = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 다리를 놓으면서 가장 가까운 섬을 찾는다.
def bfs(x, y):
    global visited
    visited = [[False] * N for _ in range(N)]
    q = deque([(x, y, 0)])
    visited[x][y] = True
    now = data[x][y]

    while q:
        x, y, b = q.popleft()
        for move in move_type:
            nx, ny = x+move[0], y+move[1]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and data[nx][ny] != now: # 모서리탐색 data[nx][ny] != now 시간복잡도 10배 빨라짐
                    visited[nx][ny] = True
                    if data[nx][ny] == 0:
                        q.append((nx, ny, b+1))
                    else:
                        return b
    return int(1e9)

# 입력받은 섬을 각각 다른 숫자로 변경
def change(x, y, count):
    q = deque([(x, y)])
    visited[x][y] = True
    data[x][y] = count

    while q:
        x, y = q.popleft()
        for move in move_type:
            nx, ny = x+move[0], y+move[1]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and data[nx][ny] == 1:
                    data[nx][ny] = count
                    visited[nx][ny] = True
                    q.append((nx, ny))


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]
count = 1
for i in range(N):
    for j in range(N):
        if not visited[i][j] and data[i][j] == 1:
            change(i, j, count)
            count += 1

min_val = int(1e9)
for i in range(N):
    for j in range(N):
        if data[i][j] != 0:
            bridge = bfs(i, j)
            min_val = min(min_val, bridge)

print(min_val)

