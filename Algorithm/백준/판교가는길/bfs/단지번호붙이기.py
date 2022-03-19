# bfs
import sys
from collections import deque
input = sys.stdin.readline

move_type = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def bfs(x, y):
    visited[x][y] = True
    q = deque([(x, y)])
    count = 1

    while q:
        x, y = q.popleft()
        for move in move_type:
            nx, ny = x + move[0], y + move[1]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and data[nx][ny]:
                    visited[nx][ny] = True
                    count += 1
                    q.append((nx, ny))
    return count


N = int(input())
data = [list(map(int, str(input().rstrip()))) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

ans = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and data[i][j]:
            ans.append(bfs(i, j))
ans.sort()
print(len(ans), *ans, sep="\n")
