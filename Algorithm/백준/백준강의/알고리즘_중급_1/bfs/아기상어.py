# 일단 bfs로 풀긴 했는데
# 이렇게 하기보단
# 먹을 수 있는걸 찾은 후
# 먹을 수 있는 고기의 모든 좌표값의 차이를 구하고
# 그 차이가 가장 작은것중 가장 왼쪽 위에있는걸 찾아서 구하면
# 훨 씬 빠를거같은데
# 사실 bfs도 안써도 될거같다

from collections import deque

move_type = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bfs(start):
    visited = [[False]*N for _ in range(N)]
    visited[start[0]][start[1]] = True
    q = deque([start+[0]])
    time = 0
    eat_cnt = 0
    shark_level = 2
    fishes = []

    while True:
        while q:
            x, y, dist = q.popleft()
            for move in move_type:
                nx, ny = move[0]+x, move[1]+y
                if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and board[nx][ny] <= shark_level:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))
                    if board[nx][ny] < shark_level and board[nx][ny] != 0:
                        fishes.append((dist+1, nx, ny))
        if fishes:
            fishes.sort()
            t, x, y = fishes[0]
            board[x][y] = 0
            time += t

            eat_cnt += 1
            if eat_cnt == shark_level:
                eat_cnt = 0
                shark_level += 1

            visited = [[False] * N for _ in range(N)]
            visited[x][y] = True
            fishes.clear()
            q.append((x, y, 0))
        else:
            return time


N = int(input())
board = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if row[j] == 9:
            row[j] = 0
            start = [i, j]
    board.append(row)

v = bfs(start)
print(v)