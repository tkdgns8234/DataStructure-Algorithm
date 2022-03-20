# for 문으로 높이 N 이하인 영역 dfs 돌리자
# dfs로 풀 수 없다. 메모리 제한때문에

import sys

sys.setrecursionlimit(100000)
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

move_type = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(x, y, k):
    visited[x][y] = True

    if data[x][y] > k:
        for move in move_type:
            nx, ny = move[0] + x, move[1] + y
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and data[nx][ny] > k:
                    dfs(nx, ny, k)
        return True
    return False


ans = 0
for k in range(1, max(map(max, data))):
    visited = [[False] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and data[i][j] > k:
                if dfs(i, j, k):
                    count += 1
    ans = max(ans, count)
print(ans)
