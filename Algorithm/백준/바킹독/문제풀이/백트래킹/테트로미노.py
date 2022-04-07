# 테트로미노

# n, m = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(n)]
# visited = [[False] * m for i in range(n)]
# ans = 0
#
# move_type = [(-1, 0), (1, 0), (0, 1), (0, -1)]
# def dfs(depth, x, y, total):
#     global ans
#     # 가지치기 하면 시간이 극적으로 줄어들어!
#     if ans >= total + (max_val * (3-depth)):
#         return
#     if depth == 3:
#         ans = max(ans, total)
#         return
#     for move in move_type:
#         nx, ny = x + move[0], y + move[1]
#         if nx < 0 or ny < 0 or nx >= n or ny >= m :
#             continue
#         if not visited[nx][ny]:
#             if depth == 1:
#                 # 다음 위치를 간것처럼 처리 후 현재 좌표 그대로 이동
#                 visited[nx][ny] = True
#                 dfs(depth + 1, x, y, data[nx][ny] + total)
#                 visited[nx][ny] = False
#             visited[nx][ny] = True
#             dfs(depth + 1, nx, ny, data[nx][ny]+total)
#             visited[nx][ny] = False
#
# max_val = max(map(max, data))
# for i in range(n):
#     for j in range(m):
#         visited[i][j] = True
#         dfs(0, i, j, data[i][j])
#         visited[i][j] = False
#
# print(ans)
