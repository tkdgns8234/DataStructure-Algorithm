# 1. 유기농 배추
# from collections import deque
# move_type = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#
# T = int(input())
#
# def dfs(x, y):
#     visited[x][y] = True
#     q = deque()
#     q.append((x, y))
#     while q:
#         x, y = q.popleft()
#         for move in move_type:
#             nx, ny = x + move[0], y + move[1]
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue
#             if not visited[nx][ny] and data[nx][ny] == 1:
#                 visited[nx][ny] = True
#                 q.append((nx, ny))
#     return
#
# for _ in range(T):
#     count = 0
#     n, m, k = map(int, input().split())
#     data = [[0] * m for i in range(n)]
#
#     for i in range(k):
#         x, y = map(int, input().split())
#         data[x][y] = 1
#
#     visited = [[False] * m for i in range(n)]
#     for i in range(n):
#         for j in range(m):
#             if not visited[i][j] and data[i][j] == 1:
#                 dfs(i, j)
#                 count += 1
#     print(count)

# 2. 적록색약
# from collections import deque
# n = int(input())
# data = [[0] * n for _ in range(n)]
# data_red_green = [[0] * n for _ in range(n)]
# for i in range(n):
#     row = list(input())
#     for j in range(len(row)):
#         data[i][j] = row[j]
#         if row[j] == 'G':
#             data_red_green[i][j] = 'R'
#         else:
#             data_red_green[i][j] = row[j]
#
# move_type = [(-1,0),(1,0),(0,1),(0,-1)]
# def dfs(x, y, arr):
#     global visited
#     q = deque()
#     q.append((x, y))
#     visited[x][y] = True
#     chr = arr[x][y]
#
#     while q:
#         x, y = q.popleft()
#         for move in move_type:
#             nx, ny = x + move[0], y + move[1]
#             if nx < 0 or ny < 0 or nx >= n or ny >= n:
#                 continue
#             if not visited[nx][ny] and arr[nx][ny] == chr:
#                 visited[nx][ny] = True
#                 q.append((nx, ny))
#
#
# for mode in range(2):
#     visited = [[False] * n for _ in range(n)]
#     cnt = 0
#     for i in range(n):
#         for j in range(n):
#             if not visited[i][j]:
#                 if mode == 0:
#                     dfs(i, j, data)
#                 else:
#                     dfs(i, j, data_red_green)
#                 cnt += 1
#     print(cnt, end=" ")

# 3. 토마토
# 문제의 키포인트 => 익은 토마토는 여러장소에 존재할 수 있음
# 처음 시작할 때 모든 익은 토마토의 위치를 큐에 넣으면 된다
# 그렇게 하지 않으면 시간복잡도가 n*m 이면 될게 (n*m) 제곱이 된다
# 그리고 구현도 힘들어진다.
# 시작할때부터 모두 익어있으면 0
# 토마토가 모두 익지는 못하는 상황이면 -1
# from collections import deque
# n, m, h = map(int, input().split())
# data = [[[0] * n for i in range(m)] for _ in range(h)]
#
# visited = [[[False] * n for i in range(m)] for _ in range(h)]
# q = deque()
#
# for k in range(h):
#     for i in range(m):
#         tmp = list(map(int, input().split()))
#         for j in range(len(tmp)):
#             data[k][i][j] = tmp[j]
#             if data[k][i][j] == 1:
#                 visited[k][i][j] = True
#                 q.append((k, i, j))
#
# move_type =[(0,1,0),(0,-1,0),(0,0,1),(0,0,-1),(1,0,0),(-1,0,0)]
# while q:
#     z,x,y = q.popleft()
#     for move in move_type:
#         nz, nx, ny = z + move[0], x + move[1], y + move[2]
#         if nx < 0 or ny < 0 or nx >= m or ny >= n or nz < 0 or nz >= h:
#             continue
#         if not visited[nz][nx][ny] and data[nz][nx][ny] == 0:
#             visited[nz][nx][ny] = True
#             data[nz][nx][ny] = data[z][x][y] + 1
#             q.append((nz,nx,ny))
#
# result = 0
# flag = False
# for k in range(h):
#     for i in range(m):
#         for j in range(n):
#             if data[k][i][j] == 0:
#                 flag = True
#                 break
#             result = max(result, data[k][i][j])
#
# if flag:
#     print(-1)
# else:
#     print(result - 1)

# 4. 불!
# 어떻게 짤지 재대로 구조를 잡지 않고 짜서 코드가 참 길고 가독성이 떨어졌다
# 백준에 제출했던 코드를 보면 알 수 있다
# 1. 일단 visited 변수를 습관적으로 두는데, 이것도 두지 않아도 될 때가 많다
# 2. 정해진 틀에서 벗어나라. 불 또는 지훈 좌표를 바로 q에 넣어도 된다 (불이 여러개가 될 수 있다는건 지문을 대충읽어서 놓치고있었다)

# from collections import deque
# import sys
# input = sys.stdin.readline
#
# def bfs():
#     while fire_q:
#         x, y = fire_q.popleft()
#         for move in move_type:
#             nx, ny = x+move[0], y+move[1]
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue
#             if data[nx][ny] == '#' or dist_fire[nx][ny] > 0:
#                 continue
#             dist_fire[nx][ny] = dist_fire[x][y] + 1
#             fire_q.append((nx,ny))
#
#     while jh_q:
#         x, y = jh_q.popleft()
#         for move in move_type:
#             nx, ny = x+move[0], y+move[1]
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 return dist_jh[x][y] + 1
#             if data[nx][ny] == '#' or dist_jh[nx][ny] > 0:
#                 continue
#             if dist_fire[nx][ny] == 0 or dist_fire[nx][ny] > dist_jh[x][y] + 1:
#                 jh_q.append((nx,ny))
#                 dist_jh[nx][ny] = dist_jh[x][y] + 1
#     return 'IMPOSSIBLE'
#
# move_type = [(-1, 0),(1, 0),(0, 1),(0, -1)]
#
# n, m = map(int, input().split())
# jh_q, fire_q = deque(), deque()
# dist_jh, dist_fire = [[0]*m for i in range(m)], [[0]*m for i in range(m)]
# data = []
# for i in range(n):
#     temp = list(input().rstrip())
#     data.append(temp)
#     for j in range(len(temp)):
#         if temp[j] == 'J':
#             jh_q.append((i,j))
#         elif temp[j] == 'F':
#             fire_q.append((i,j))
#
# print(bfs())

# 5. 나이트의 이동
# from collections import deque
# import sys
# input = sys.stdin.readline
# T = int(input())
# # 묶기
# for _ in range(T):
#     size = int(input())
#     data = [[0] * size for i in range(size)]
#     now_x,now_y = map(int, input().rstrip().split())
#     target_x,target_y = map(int, input().rstrip().split())
#     data[now_x][now_y] = 1 # 방문한곳 = 1 이상 거리별 증가
#     data[target_x][target_y] = -2 # 타겟 = -2
#
#     if now_x == target_x and now_y == target_y:
#         print(0)
#         continue
#
#     move_type = [
#         (-1, 2),(-2, 1),(-1, -2),(-2, -1),(1, 2),(2, 1),(2, -1),(1, -2)
#     ]
#     q = deque()
#     q.append((now_x,now_y))
#     flag = False
#     while q:
#         x, y = q.popleft()
#         for move in move_type:
#             nx, ny = x + move[0], y + move[1]
#             if nx < 0 or ny < 0 or nx >= size or ny >= size:
#                 continue
#             if data[nx][ny] == 0:
#                 data[nx][ny] = data[x][y] + 1
#                 q.append((nx,ny))
#             if data[nx][ny] == -2:
#                 print(data[x][y])
#                 flag = True
#                 break
#         if flag:
#             break

# 6. 불
# from collections import deque
# import sys
# input = sys.stdin.readline
#
# move_type = [(-1,0),(1,0),(0,1),(0,-1)]
# def bfs():
#     while fire_q:
#         x, y = fire_q.popleft()
#         for move in move_type:
#             nx, ny = move[0] + x, move[1] + y
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue
#             if data[nx][ny] != '#' and data[nx][ny] != '*' and fire_dist[nx][ny] == 0:
#                 fire_dist[nx][ny] = fire_dist[x][y] + 1
#                 fire_q.append((nx, ny))
#
#     while sg_q:
#         x, y = sg_q.popleft()
#         for move in move_type:
#             nx, ny = move[0] + x, move[1] + y
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 return sg_dist[x][y] + 1
#             if sg_dist[nx][ny] > 0 or data[nx][ny] == '#' or data[nx][ny] == '*' or data[nx][ny] == '@':
#                 continue
#             if fire_dist[nx][ny] == 0 or fire_dist[nx][ny] > sg_dist[x][y] + 1:
#                 sg_dist[nx][ny] = sg_dist[x][y] + 1
#                 sg_q.append((nx,ny))
#     return 'IMPOSSIBLE'
#
#
# T = int(input().rstrip())
# for _ in range(T):
#     m, n = map(int, input().rstrip().split()) #n x m y
#     sg_q, fire_q = deque(), deque()
#     sg_dist, fire_dist = [[0] * m for i in range(n)], [[0] * m for i in range(n)]
#     data = []
#
#     for i in range(n):
#         temp = list(input().rstrip())
#         data.append(temp)
#         for j in range(len(temp)):
#             if temp[j] == '@':
#                 sg_q.append((i,j))
#             elif temp[j] == '*':
#                 fire_q.append((i,j))
#
#     print(bfs())

# 7. 벽 부수고 이동하기
# 풀이가 쉽게 떠오르지 않아 블로그를 참조했다
# 3차원 형식의 bfs 문제였다
# bfs, dfs는 완전탐색알고리즘의 일종이다
# 따라서 모든곳을 탐색하게 되고, 벽을 한번만 뚫도록 구현하는것도 3차원 배열을 이용하면 가능하다
# 벽돌을 부순 큐의 dist 가 겹쳐도 되나? 결국 가장 빨리 도착하는것이 최단거리 인것인가
# 벽돌을 부순 경우에대한 dist를 동일하게 써서 이미 방문한곳을 방문하지 않도록 하는게 맞는지 증거하는게 어려웠다
# => 이에대한 답은 만약 먼저 출발한 벽돌 꺤 큐가 목적지까지 도착하지 못한다면 그 뒤에오는 벽돌 꺤 큐도
# 같은 길로 간다면 도착하지 못하게되므로 동일한 dist 를 사용해서 이미 방문한곳을 방문하지 못하게 해도 된다.
# 아주 좋은 문제였다
# import sys
# from collections import deque
# input = sys.stdin.readline
# move_type = [(-1,0),(1,0),(0,1),(0,-1)]
# n, m = map(int, input().rstrip().split())
# data = []
# for i in range(n):
#     temp = list(map(int, list(input().rstrip())))
#     data.append(temp)
# dist = [[[0] * 2 for i in range(m)] for _ in range(n)]  # 벽돌 부순것과 부수지 않은것
#
# q = deque()
# q.append((0, 0, 0)) # 0 = wall 을 깨지않은상태 1 = 깬 상태
# dist[0][0][0] = 1
# while q:
#     x, y, wall = q.popleft()
#     if x == n-1 and y == m-1:
#         print(dist[x][y][wall])
#         exit(0)
#     for move in move_type:
#         nx, ny = x + move[0], y + move[1]
#         if 0 <= nx < n and 0 <= ny < m and dist[nx][ny][wall] == 0:
#             if data[nx][ny] == 1:  # 벽인 경우
#                 if wall == 0: # 벽돌을 깬적이 없는 경우
#                     q.append((nx,ny,1))  # 1 은 벽돌을 깬 경우로 표시, 이동
#                     dist[nx][ny][1] = dist[x][y][wall] + 1
#             else:
#                 q.append((nx,ny,wall))
#                 dist[nx][ny][wall] = dist[x][y][wall] + 1
# print(-1)

# 8. 텀 프로젝트
# 실패 dfs 정말 어렵다.. 재귀형식
# import sys
# input = sys.stdin.readline
# def dfs(start, index, count):
#     global visited
#     if start != index and visited[index]:
#         return 0
#     if count != 0 and start == index:
#         return count
#     visited[index] = True
#     return dfs(start, data[index], count + 1)
#
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     data = [None] + list(map(int, input().split()))
#     visited = [False] * (n + 1)
#     ans = 0
#
#     for i in range(1, len(data)):
#         if not visited[i]:
#             ans += dfs(i, i, 0)
#     print(ans)


# 아래는 참고한 dfs 소스
# import sys
#
# sys.setrecursionlimit(10 ** 7)
#
# input = sys.stdin.readline
#
#
# def dfs(x):
#     global ans
#     vis[x] = True
#     cycle.append(x)
#     num = arr[x]
#
#     if vis[num]:
#         if num in cycle:
#             ans += cycle[cycle.index(num):]
#         return
#     else:
#         dfs(num)
#
#
# t = int(input())
#
# for _ in range(t):
#     n = int(input())
#     arr = [0] + list(map(int, input().split()))
#     vis = [False] * (n + 1)
#     ans = []
#
#     for i in range(1, n + 1):
#         if not vis[i]:
#             cycle = []
#             dfs(i)
#
#     print(n - len(ans))

# 다시풀기
# 성공
# import sys
# sys.setrecursionlimit(100001)
#
# def dfs(index):
#     global ans
#     visited[index] = True
#     cycle.append(index)
#     num = data[index]
#     if visited[num]:
#         if num in cycle:
#             return len(cycle[cycle.index(num):])
#         else:
#             return 0
#     return dfs(num)
#
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     data = [None] + list(map(int, input().split()))
#     visited = [False] * (n + 1)
#     ans = 0
#
#     for i in range(1, len(data)):
#         if not visited[i]:
#             cycle = []
#             ans += dfs(i)
#     print(len(data)-ans-1)

# 9. 빙산
# 얼음을 녹인 후 bfs로 탐색하자
# 시간이 2000ms가 소요된다
# 짧게는 800ms 까지 가능한것같은데
# 다시풀자
# 좀 더 효율적인 bfs 방법이 분명 있어보여
# 개선을 거친 코드

# from collections import deque
# import sys
# input = sys.stdin.readline  # 개선포인트 0
# move_type = [(-1, 0), (1, 0), (0, 1), (0, -1)]
#
# def ice_to_water():
#     melt = []  # 개선포인트 1 기존엔 temp 배열을가지고 딥카피 하는식으로 했었음, 비효율적이었음
#     for x in range(n):  # for문을 함수 내에서 직접호출.
#         for y in range(m):
#             water_cnt = 0
#             if data[x][y] != 0:
#                 for move in move_type:
#                     nx, ny = x + move[0], y + move[1]
#                     if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                         continue
#                     if data[nx][ny] == 0:
#                         water_cnt += 1
#                     melt.append((x, y,  max(0, data[x][y] - water_cnt))) #최솟값은 0
#     for a, b, c in melt:
#         data[a][b] = c
#
# def bfs():
#     cnt = 0
#     visited = [[False] * m for _ in range(n)]
#     for i in range(n):  # for문을 함수 내에서 직접호출.
#         for j in range(m):
#             if not visited[i][j] and data[i][j] != 0:
#                 cnt += 1
#                 visited[i][j] = True
#                 q = deque()
#                 q.append((i, j))
#                 while q:
#                     x, y = q.popleft()
#                     for move in move_type:
#                         nx, ny = x + move[0], y + move[1]
#                         if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                             continue
#                         if data[nx][ny] > 0 and not visited[nx][ny]:
#                             visited[nx][ny] = True
#                             q.append((nx, ny))
#     return cnt
#
#
# n, m = map(int, input().split())
# data = [list(map(int, input().split())) for i in range(n)]
# passed = 0
# while True: # 개선포인트 2 while 문을 조금 더 단순화, 함수안에서 필요한것들을 모두 처리, 중복 for문등 다 함수 안으로
#     cnt = bfs()
#     if cnt >= 2:
#         print(passed)
#         break
#     elif cnt == 0:
#         print(0)
#         break
#
#     ice_to_water()
#     passed += 1

# 훨씬 더 좋아보이는 코드
# count 라는 변수를 둬서 주변의 water count를 센다.
# import sys
# from collections import deque
#
# input = sys.stdin.readline
# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))
#
# check = False
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
#
# def bfs(x, y):
#     q = deque()
#     q.append([x, y])
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < m:
#                 if graph[nx][ny] == 0:
#                     count[x][y] += 1
#                 elif graph[nx][ny] != 0 and not visited[nx][ny]:
#                     visited[nx][ny] = True
#                     q.append([nx, ny])
#     return 1
#
#
# year = 0
# while True:
#     visited = [[False] * m for _ in range(n)]
#     count = [[0] * m for _ in range(n)]
#     result = []
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] != 0 and not visited[i][j]:
#                 visited[i][j] = True
#                 result.append(bfs(i, j))
#
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] != 0:
#                 graph[i][j] -= count[i][j]
#                 if graph[i][j] < 0:
#                     graph[i][j] = 0
#
#     if len(result) == 0:
#         break
#     if len(result) >= 2:
#         check = True
#         break
#     year += 1
#
# if check:
#     print(year)
# else:
#     print(0)

# 10. 다리 만들기
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

# 문제 11 숨바꼭질
# 최단거리 문제이기떄문에 bfs 로 해결
# 목표지점까지 발생하는 비용이 다르기때문에 *2 를 먼저처리해야한다(다익스트라 알고리즘을 떠올려보자 원리는 동일하다)
# 연산 또한 곱셈 부터 처리해야한다 큐에만 먼저 넣는다고 되는것이 아니다 //반례: 1 3

# from collections import deque
# import sys
# PLUS = 2
# MINUS = 1
# MULTIPLE = 0
# n, target = map(int, sys.stdin.readline().split())
# visited = [False] * 200001
#
# q = deque()
# q.append((n, 0))
# visited[n] = True
# while q:
#     x, time = q.popleft()
#     if x == target:
#         print(time)
#         break
#     for oper in range(3):
#         temp = time
#         nx = x
#         if oper == PLUS:
#             nx, temp = nx + 1, temp + 1
#         elif oper == MINUS:
#             nx, temp = nx - 1, temp + 1
#         elif oper == MULTIPLE:
#             nx = x * 2
#         if 0 <= nx <= 200000 and not visited[nx]:
#             visited[nx] = True
#             if oper == MULTIPLE:
#                 q.appendleft((nx, temp))
#             else:
#                 q.append((nx, temp))


# 아래 코드처럼 방문 확인을 가중치 형태로 하면 원하는 답을 얻을 수 있기도 하다
# 개선된 다익스트라에선 visited 가 아니라 dist 로 이미 방문했는지 확인했었지. 여기서말하는 가중치가 dist 와 동일해
# 가중치 (dist)가 더 짧다면 이미 처리된 노드로 방문 처리

# from collections import deque
# def bfs(x):
#     q = deque([x])		# 다익스트라와 달리 가중치(시간) 없음!
#     time = [-1] * MAX		# 중복방문을 위한 가중치행렬
#     time[x] = 0
#
#     while q:
#         cx = q.popleft()
#         if cx == k:
#             return time[cx]
#
#         for i in range(3):
#             if i == 0:
#                 nx = cx - 1
#             elif i == 1:
#                 nx = cx + 1
#             else:
#                 nx = cx * 2
#
#             if not 0 <= nx < MAX:	# 조건 검사 역시 다익스트라와 동일
#                 continue
#             if time[nx] != -1 and time[nx] <= time[cx]:
#                 continue
#
#             if i < 2:			# 한 칸씩 이동하는 경우 큐 뒤에 삽입
#                 q.append(nx)
#                 time[nx] = time[cx] + 1
#             else:			# 순간이동하는 경우 큐 앞에 삽입
#                 q.appendleft(nx)
#                 time[nx] = time[cx]
#
#
# n, k = map(int, input().split())
# MAX = 100001
# print(bfs(n))

# 문제 12 말이 되고픈 원숭이
# 벽돌 부수기와 매우 유사해보여 말처럼 이동한 횟수를 3차원배열 위치에 표시하도록 해보자
# import sys
# from collections import deque
# input = sys.stdin.readline
#
# move_type = [(-1, 0), (1, 0), (0, 1), (0, -1)]
# horse_move_type = [(-1, -2), (-2, -1), (-2, 1), (-1, 2),
#       (1, -2), (2, -1), (2, 1), (1, 2)]
#
# k = int(input())
# m, n = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(n)]
#
# dist = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]
# dist[0][0][0] = 1
#
# q = deque()
# q.append((0,0,0))
#
# while q:
#     x, y, horse = q.popleft()
#     if x == n-1 and y == m-1:
#         print(dist[x][y][horse]-1)
#         exit(0)
#     for move in move_type:
#         nx, ny = x + move[0], y + move[1]
#         if nx < 0 or ny < 0 or nx >= n or ny >= m:
#             continue
#         if data[nx][ny] == 0 and dist[nx][ny][horse] == 0:
#             dist[nx][ny][horse] = dist[x][y][horse] + 1
#             q.append((nx, ny, horse))
#     if horse < k:
#         for move in horse_move_type:
#             nx, ny = x + move[0], y + move[1]
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue
#             if data[nx][ny] == 0 and dist[nx][ny][horse+1] == 0:
#                 dist[nx][ny][horse+1] = dist[x][y][horse] + 1
#                 q.append((nx, ny, horse+1))
#
# print(-1)