N = int(input())
data = [list(map(int, str(input()))) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

move_type = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def dfs(x, y):
    visited[x][y] = True

    if data[x][y] == 1:
        global count
        count += 1
        for move in move_type:
            nx, ny = move[0] + x, move[1] + y
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny]:
                    dfs(nx, ny)
        return True
    return False


count = 0
ans = 0
nums = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and data[i][j] == 1:
            if dfs(i, j):
                nums.append(count)
            ans += 1
            count = 0
nums.sort()
print(ans, *nums, sep="\n")