# 분명히 1000*1000*10 이면 시간복잡도를 충분히 만족할거라 생각했는데
# 계속 시간초과가 발생해서 애먹었던 문제다

# 그저 구현 실수였다..
# visit 처리는 다음 방문할 위치를 확인하는것
# visit 처리를 할 때 항상 if visited[nx][ny][wall] == 0 으로 방문 처리를 했는데
# 다음 위치가 벽인경우와 벽이 아닌경우로 나눠서 방문 처리를 해줘야한다.

import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]

ans = -1
q = deque([[0, 0, 0]])
visited[0][0][0] = 1
while q:
    x, y, wall = q.popleft()
    if x == N-1 and y == M-1:
        ans = visited[x][y][wall] # 시작위치포함
        break
    for move in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        nx, ny = x+move[0], y+move[1]
        if 0<=nx<N and 0<=ny<M:
            if board[nx][ny] == 1:
                if wall < K and visited[nx][ny][wall+1] == 0:
                    visited[nx][ny][wall+1] = visited[x][y][wall]+1
                    q.append((nx, ny, wall+1))
            else:
                if visited[nx][ny][wall] == 0:
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    q.append((nx, ny, wall))

print(ans)