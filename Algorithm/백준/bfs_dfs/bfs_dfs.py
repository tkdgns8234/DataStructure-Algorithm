# 문제1 그림
# from collections import deque
#
# move_type = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#
#
# def bfs(x, y, visited):
#     global max_size
#     q = deque()
#     q.append((x, y))
#     visited[x][y] = True
#     cnt = 0
#     while q:
#         x, y = q.popleft()
#         cnt += 1
#         for move in move_type:
#             nx, ny = x + move[0], y + move[1]
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue
#             if not visited[nx][ny] and graph[nx][ny] == 1:
#                 visited[nx][ny] = True
#                 q.append((nx, ny))
#     if cnt > 0:
#         max_size = max(max_size, cnt)
#         return True
#
#
# n, m = map(int, input().split())
#
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))
#
# max_size = 0
# count = 0
# visited = [[False] * m for _ in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 1 and not visited[i][j]:
#             if bfs(i, j, visited):
#                 count += 1
#
# print(count, max_size, end="\n")

# 문제2 미로탐색
# from collections import deque
# n, m = map(int, input().split())
#
# data = []
# for _ in range(n):
#     data.append(list(map(int, str(input()))))
#
# visited = [[False] * m for _ in range(n)]
#
# q = deque()
# q.append((0, 0))
# visited[0][0] = True
#
# move_type = [(-1, 0), (1, 0), (0, 1), (0, -1)]
# while q:
#     x, y = q.popleft()
#     for move in move_type:
#         nx, ny = move[0] + x, move[1] + y
#         if nx < 0 or ny < 0 or nx >= n or ny >= m:
#             continue
#         if not visited[nx][ny] and data[nx][ny] == 1:
#             visited[nx][ny] = True
#             q.append((nx, ny))
#             data[nx][ny] = data[x][y] + 1
#
# print(data[n-1][m-1])
#

# 문제3 토마토
# from collections import deque
# m, n = map(int, input().split())
#
# data = []
# for i in range(n):
#     data.append(list(map(int, input().split())))
#
# visited = [[False] * m for _ in range(n)]
#
# q = deque()
#
# for i in range(n):
#     for j in range(m):
#         if data[i][j] == 1:
#             q.append((i, j))
#             visited[i][j] = True
#
# move_type = [(-1, 0), (1, 0), (0, 1), (0, -1)]
# while q:
#     x, y = q.popleft()
#     for move in move_type:
#         nx, ny = x + move[0], y + move[1]
#         if nx < 0 or ny < 0 or nx >= n or ny >= m:
#             continue
#         if data[nx][ny] == 0 and not visited[nx][ny]:
#             visited[nx][ny] = True
#             q.append((nx, ny))
#             data[nx][ny] = data[x][y] + 1
#
#
# for i in range(n):
#     for j in range(m):
#         if data[i][j] == 0:
#             print(-1)
#             exit(0)
# print(max(map(max, data)) - 1)

# 문제4 숨바꼭질
# from collections import deque
#
# n, m = map(int, input().split())
# visited = [False] * 100001
#
# q = deque()
# q.append((n, 0))
# visited[n] = True
#
# move_type = [1, -1, 2]
# while q:
#     now, time = q.popleft()
#     if now == m:
#         print(time)
#         break
#
#     for move in move_type:
#         if move == 2:
#             n_now = now * 2
#         else:
#             n_now = now + move
#         if 0 <= n_now <= 100000 and not visited[n_now]:
#             visited[n_now] = True
#             q.append((n_now, time + 1))
