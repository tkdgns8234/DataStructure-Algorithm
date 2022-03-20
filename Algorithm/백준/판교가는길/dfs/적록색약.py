import sys
import copy
sys.setrecursionlimit(10000)

N = int(input())
data = []
data_rg_same = []
for i in range(N):
    temp = list(str(input()))
    data.append(copy.deepcopy(temp))
    for j in range(N):
        if temp[j] == 'G':
            temp[j] = 'R'
    data_rg_same.append(temp)

visited = [[False] * N for _ in range(N)]
visited_rg_same = [[False] * N for _ in range(N)]

move_type = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(x, y, visited_, data_, char):
    visited_[x][y] = True

    if data_[x][y] == char:
        for move in move_type:
            nx, ny = x + move[0], y + move[1]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited_[nx][ny] and data_[nx][ny] == char:
                    dfs(nx, ny, visited_, data_, char)
        return True
    return False


count = [0, 0]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            if dfs(i, j, visited, data, data[i][j]):
                count[0] += 1
        if not visited_rg_same[i][j]:
            if dfs(i, j, visited_rg_same, data_rg_same, data_rg_same[i][j]):
                count[1] += 1

print(count[0], count[1], sep=" ")
