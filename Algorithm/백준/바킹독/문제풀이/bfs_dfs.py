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
