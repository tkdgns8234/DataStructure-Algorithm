# 10. 다리 만들기
# 최근에 다시 푼게 존재함.
# 판교가는길 폴더 내의 bfs 문제 확인



# 성공했지만 시간, 공간복잡도가 너무 비효율적이야
# 좀 더 효율적인 방법을 찾아보자
# import copy
# from collections import deque
# n = int(input())
# data = [list(map(int, input().split())) for i in range(n)]
# move_type = [(-1, 0), (1, 0), (0, 1), (0, -1)]
#
# def bfs (x, y):
#     visited[x][y] = True
#     visited2[x][y] = True
#     point.append((x,y))
#     q = deque()
#     q.append((x, y))
#     while q:
#         x, y = q.popleft()
#         for move in move_type:
#             nx, ny = x + move[0], y + move[1]
#             if nx < 0 or ny < 0 or nx >= n or ny >= n:
#                 continue
#             if not visited[nx][ny] and data[nx][ny] == 1:
#                 q.append((nx, ny))
#                 point.append((nx, ny))
#                 visited[nx][ny] = True
#                 visited2[nx][ny] = True
#
# def make_bridge(x, y):
#     temp = copy.deepcopy(visited2)
#     q = deque()
#     q.append((x, y, 0))
#     while q:
#         x, y, dist = q.popleft()
#         for move in move_type:
#             nx, ny = x + move[0], y + move[1]
#             if nx < 0 or ny < 0 or nx >= n or ny >= n:
#                 continue
#             if not temp[nx][ny]:
#                 if data[nx][ny] == 1:
#                     return dist
#                 else:
#                     q.append((nx, ny, dist+1))
#                     temp[nx][ny] = True
#     return int(1e9) # 못 찾은경우
#
# # 섬 찾기 # 찾은경우 모두 방문표시
# min_val = int(1e9)
# visited =[[False] * n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if not visited[i][j] and data[i][j] == 1:
#             visited2 = [[False] * n for _ in range(n)]
#             point = []
#             bfs(i, j)
#
#             for a, b in point:
#                 min_val = min(min_val, make_bridge(a, b))
#
# print(min_val)

# 다리 만들기 참고 코드
# 와... 이렇게 풀 수 있구나 결국 문제에서 요구하는건 각 섬 좌표간의 최단거리만 구하면 되니까
# x1-x2 + y1-y2 - 1 => 최단거리
# 아래 코드의 풀이 방식 1. 각 섬마다 [[]] 배열을 하나 만들고 좌표를 모두 저장
# 각 좌표간의 차이중 최솟값을 print 아주 간단해..
# 문제의 핵심을 이해하고 아주 효율적으로 짰어

# import sys
# import collections
# import itertools
# import heapq
#
# dy = [1, 0, -1, 0]
# dx = [0, 1, 0, -1]
#
# R = lambda : sys.stdin.readline().rstrip()
# MIS = lambda : map(int, R().split())
#
# N = int(R())
# L = [list(MIS()) for _ in range(N)]
# visited = [[0]*N for _ in range(N)]
# num = 1
# t = []
# que = collections.deque()
# for i in range(N):
#     for j in range(N):
#         if visited[i][j] or L[i][j] == 0: continue
#         que.append((i, j))
#         visited[i][j] = num
#         t.append([])
#         t[-1].append((i, j))
#         while que:
#             y, x = que.pop()
#             for d in range(4):
#                 ry = y+dy[d]
#                 rx = x+dx[d]
#                 if 0 <= ry < N and 0 <= rx < N and visited[ry][rx] == 0 and L[ry][rx]:
#                     visited[ry][rx] = num
#                     que.append((ry, rx))
#                     t[-1].append((ry, rx))
#         num += 1
#
# ans = 100000
# for i in range(len(t)):
#     for j in range(i+1, len(t)):
#         for a, b in t[i]:
#             for x, y in t[j]:
#                 ans = min(ans, abs(a-x)+abs(b-y)-1)
# print(ans)

# 다리만들기 참고 코드
# 내가 풀었던 방식과 유사하나
# 훨씬 빠르고 공간복잡도가 좋았던 이유:
# 포인트는 2개다
# 1. 입력받은 지도의 섬을 구분하기위해 섬1 = 1로표시하고 섬2 =2로표시하도록 했다
# = > visited 는 하나면되고 입력받은 지도의 섬 좌표를 1,2,3 으로 나타내는방식
# 2. 모든 좌표에서 최단거리를 구하는건 동일한데,
# 나는 각 좌표마다 따로 돌았고 이사람은 모든 좌표를 한번에 넣어서 돌렸다 최단거리 찾는걸

# from collections import deque
#
# def boundary(r, c):
#     if (0 <= r < N) and (0 <= c < N):
#         return True
#     return False
#
# def find_island(i, sr, sc):
#     result = deque()
#
#     visit[sr][sc] = True
#
#     que = deque()
#     que.append((sr, sc))
#
#     while que:
#         nr, nc = que.popleft()
#         board[nr][nc] = i
#         result.append((nr, nc, 0))
#
#         for d in dx:
#             nxr, nxc = nr + d[0], nc + d[1]
#             if not boundary(nxr, nxc) or board[nxr][nxc] == 0 or visit[nxr][nxc]:
#                 continue
#
#             visit[nxr][nxc] = True
#             board[nxr][nxc] = i
#             que.append((nxr, nxc))
#
#     return result
#
#
# def find_bridge(island, i):
#     visit = [[False] * N for _ in range(N)]
#
#     while island:
#         nr, nc, nl = island.popleft()
#
#         for d in dx:
#             nxr, nxc, nxl = nr + d[0], nc + d[1], nl + 1
#             if not boundary(nxr, nxc) or board[nxr][nxc] == i or visit[nxr][nxc]:
#                 continue
#
#             if board[nxr][nxc] > 0:
#                 return nl
#             else:
#                 visit[nxr][nxc] = True
#                 island.append((nxr, nxc, nxl))
#
#
# dx = ((-1, 0), (1, 0), (0, -1), (0, 1))
# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
#
# islands = [None]
# visit = [[False] * N for _ in range(N)]
# for r in range(N):
#     for c in range(N):
#         if board[r][c] == 1 and not visit[r][c]:
#             islands.append(find_island(len(islands), r, c))
#
# ans = N ** 2
# for i in range(1, len(islands)):
#     island = islands[i]
#     ans = min(find_bridge(island, i), ans)
#
# print(ans)
