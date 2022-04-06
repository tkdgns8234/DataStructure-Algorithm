# 와 백트래킹 없이 푼 풀이인데
# 정말 신기하다;
# set 연산도 활용
#
# from itertools import combinations
# from collections import deque
# import sys
# import copy
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
#
# def bfs(array, selected, green):
#     cnt = 0
#     green_q = deque()
#     red_q = deque()
#
#     for row, col in selected:
#         if [row, col] in green:
#             green_q.append([row, col])  # 초록색 배양액
#             array[row][col] = 3
#         else:
#             red_q.append([row, col])  # 빨간색 배양액
#             array[row][col] = 4
#
#     while green_q:  # 초록색 배양액이 빌때까지
#         green_temp = set()
#         red_temp = set()
#         while green_q:
#             x, y = green_q.popleft()
#             array[x][y] = 3
#             for i in range(4):
#                 new_x, new_y = x + dx[i], y + dy[i]
#                 if 0 <= new_x < n and 0 <= new_y < m:
#                     if array[new_x][new_y] == 1 or array[new_x][new_y] == 2:
#                         green_temp.add((new_x, new_y))
#         while red_q:
#             x, y = red_q.popleft()
#             array[x][y] = 4
#             for i in range(4):
#                 new_x, new_y = x + dx[i], y + dy[i]
#                 if 0 <= new_x < n and 0 <= new_y < m:
#                     if array[new_x][new_y] == 1 or array[new_x][new_y] == 2:
#                         red_temp.add((new_x, new_y))
#
#         inter = green_temp & red_temp
#         green_temp = green_temp - inter
#         red_temp = red_temp - inter
#         for row, col in inter:
#             array[row][col] = 5
#             cnt += 1
#         for row, col in green_temp:
#             array[row][col] = 3
#         for row, col in red_temp:
#             array[row][col] = 4
#         green_q.extend(green_temp)
#         red_q.extend(red_temp)
#
#     return cnt
#
#
# if __name__ == "__main__":
#     n, m, g, r = map(int, sys.stdin.readline().split())
#     maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
#
#     # 배양액을 뿌릴 수 있는 위치, 뿌릴 수 없는 위치 탐색
#     location = []
#     for i in range(n):
#         for j in range(m):
#             if maps[i][j] == 2:
#                 location.append([i, j])
#
#     answer = 0
#     for selected in list(combinations(location, g + r)):
#         # selected를 green과 red로 나누기
#         for green in list(combinations(selected, g)):
#             copy_maps = copy.deepcopy(maps)
#             answer = max(answer, bfs(copy_maps, selected, green))
#
#     # 출력
#     print(answer)


# 백트래킹을 사용한 풀이
# 재귀, 백트래킹, dp가 많이 어렵긴하다 구조 자체가

# from sys import stdin
# from collections import deque
# from itertools import combinations
#
# input = stdin.readline
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# INF = 9876543210
#
# n,m,g,r = map(int, input().split())
# board = []
# candidate = []
# for x in range(n):
#     board.append(list(map(int, input().split())))
#     for y in range(m):
#         if board[x][y] == 2:
#             candidate.append((x,y))
#
# answer = 0
# def solv():
#     select = [0]*(g+r)
#     for pos in combinations(candidate,g+r):
#         select_color(select,0,pos,[g,r])
#     print(answer)
# def select_color(select,now,pos,cnt):
#     global answer
#     if now == g+r:
#         print(select, pos)
#         answer = max(answer, simul(pos, select))
#         return
#
#     if cnt[0] > 0:
#         cnt[0] -= 1
#         select[now] = 1
#         select_color(select,now+1,pos,cnt)
#         cnt[0] += 1
#
#     if cnt[1] > 0:
#         cnt[1] -= 1
#         select[now] = -1
#         select_color(select,now+1,pos,cnt)
#         cnt[1] += 1
#
# def simul(pos, order):
#     visited = [[0] * m for _ in range(n)]
#     q = deque()
#
#     for idx in range(g+r):
#         x,y = pos[idx]
#         color = order[idx]
#         visited[x][y] = color
#         q.appendleft((x, y, color))
#
#     flower_count = 0
#     while q:
#         x,y,t = q.pop()
#
#         if visited[x][y] == INF:
#             continue
#
#         for d in range(4):
#             nx = x + dx[d]
#             ny = y + dy[d]
#
#             if point_validator(nx,ny,visited):
#                 if visited[nx][ny] == 0:
#                     if t < 0:
#                         visited[nx][ny] = t-1
#                         q.appendleft((nx,ny,t-1))
#                     else:
#                         visited[nx][ny] = t+1
#                         q.appendleft((nx,ny,t+1))
#                 elif abs(visited[nx][ny]) == abs(t)+1 and ((visited[nx][ny] < 0 and t > 0) or (visited[nx][ny] > 0 and t < 0)):
#                     flower_count += 1
#                     visited[nx][ny] = INF
#     return flower_count
# def point_validator(x,y,visited):
#     if x < 0 or y < 0 or x >= n or y >= m:
#         return False
#     elif visited[x][y] == INF:
#         return False
#     elif board[x][y] == 0:
#         return False
#     return True
# solv()

