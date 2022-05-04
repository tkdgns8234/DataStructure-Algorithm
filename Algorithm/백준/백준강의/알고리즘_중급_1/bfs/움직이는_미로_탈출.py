# 실패
# from collections import deque
#
# board = [list(input()) for _ in range(8)]
# visited = [[0]*8 for _ in range(8)]
#
# def move_stone(board):
#     board.pop()
#     board.insert(0, [0 for i in range(8)])
#
# def bfs(x, y):
#     q = deque([[x, y, 0]])
#     visited[x][y] = 1
#     s = 0
#     while q:
#         x, y, sec = q.popleft()
#         if x == 0 and y == 7:
#             return 1
#         if sec != s:
#             move_stone(board)
#             s = sec
#         if board[x][y] == '#':
#             continue
#         move_type = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1), (1, 1), (-1, -1)]
#         for move in move_type:
#             nx, ny = x + move[0], y + move[1]
#             if 0<=nx<8 and 0<=ny<8 and not visited[nx][ny]:
#                 # 이동하려는 위치의 위쪽에 벽이 없는 경우 이동 가능
#                 if board[nx][ny] != '#':
#                     visited[nx][ny] = 1
#                     q.append([nx, ny, sec + 1])
#         if visited[x][y] < 7:
#             if x > 1 and board[x-1][y] != "#":
#                 visited[x][y] += 1
#                 q.append([x, y, sec+1])
#     return 0
# rs = bfs(7, 0)
# print(rs)


# 뭘 한거지..
# visit 처리를 하면 안됐다..
# 기다렸다 가야만 성공하는 경우도 있잖아;
# 지금 최단거리로 가는게 아니잖아 일단
# 기다렸다가 가도, 도착만 할 수 있다면 되는거야...
# 문제 파악 자체를 잘못했어
# 성공 코드
from collections import deque

# board = [list(input()) for _ in range(8)]
#
# def move_stone(board):
#     board.pop()
#     board.insert(0, [0 for i in range(8)])
#
# def bfs(x, y):
#     q = deque([[x, y, 0]])
#     s = 0
#     while q:
#         x, y, sec = q.popleft()
#         if x == 0 and y == 7 or sec == 8:
#             return 1
#         if sec != s:
#             move_stone(board)
#             s = sec
#         if board[x][y] == '#':
#             continue
#         move_type = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1), (1, 1), (-1, -1)]
#         for move in move_type:
#             nx, ny = x + move[0], y + move[1]
#             if 0<=nx<8 and 0<=ny<8:
#                 # 이동하려는 위치의 위쪽에 벽이 없는 경우 이동 가능
#                 if board[nx][ny] != '#':
#                     q.append([nx, ny, sec + 1])
#     return 0
# rs = bfs(7, 0)
# print(rs)


# 다른 방법
# 한번에 q에 들어간 양만큼 처리하는 방법
from collections import deque
#
# board = [list(input()) for _ in range(8)]
#
# def move_stone(board):
#     board.pop()
#     board.insert(0, [0 for i in range(8)])
#
# def bfs(x, y):
#     q = deque([[x, y]])
#     cnt = 0
#     while q:
#         len_q = len(q)
#         for _ in range(len_q):
#             x, y = q.popleft()
#             if x == 0 and y == 7:
#                 return 1
#             if board[x][y] == '#':
#                 continue
#             move_type = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1), (1, 1), (-1, -1)]
#             for move in move_type:
#                 nx, ny = x + move[0], y + move[1]
#                 if 0<=nx<8 and 0<=ny<8:
#                     # 이동하려는 위치의 위쪽에 벽이 없는 경우 이동 가능
#                     if board[nx][ny] != '#':
#                         q.append([nx, ny])
#         move_stone(board)
#         cnt += 1
#         # print(cnt)
#         if cnt == 9:
#             return 1
#     return 0
# rs = bfs(7, 0)
# print(rs)



# 신기한 풀이

# from collections import deque
# input = __import__('sys').stdin.readline
# n = 8
# graph = [list(input().strip()) for _ in range(n)]
# visited = [[False] * n for _ in range(n)]
# dx = [0, 0, 1, -1, 1, -1, 1, -1, 0]
# dy = [1, -1, 0, 0, 1, 1, -1, -1, 0]
#
# q = deque()
# q.append((7, 0))
# visited[7][0] = True
# ans = 0
# while q:
#     i, j = q.popleft()
#     if graph[i][j] == '#':
#         continue
#     for idx in range(n + 1):
#         ni = i + dy[idx]
#         nj = j + dx[idx]
#         if ni < 0 or ni >= n or nj < 0 or nj >= n or graph[ni][nj] == '#':
#             continue
#         if ni == 0:
#             ans = 1
#         if not visited[ni - 1][nj]:
#             visited[ni - 1][nj] = True
#             q.append((ni - 1, nj))
# print(ans)