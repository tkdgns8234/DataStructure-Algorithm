# Q31 금광
# bfs 말고 그냥 구현문제처럼 풀 수 있다 점화식세워서 다시풀어보자

# move_type = [(-1,1), (0, 1), (1, 1)]
#
# import copy
# from  collections import deque
# def find_maximum_path(data, x, y):
#     n = len(data)
#     m = len(data[0])
#     result = copy.deepcopy(data)
#     q = deque()
#     q.append((x, y))
#
#     while q:
#         x, y = q.popleft()
#         for move in move_type:
#             nx = x + move[0]
#             ny = y + move[1]
#
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue
#
#             result[nx][ny] = max(result[nx][ny], result[x][y] + data[nx][ny])
#             q.append((nx, ny))
#
#     return max(map(max, result))
#
#
#
#
# t = int(input())
# for i in range(t):
#     n, m = map(int, input().split())
#     l = list(map(int, input().split()))
#     data = []
#     for i in range(0, len(l), m):
#         data.append(l[i:i+m])
#     max_val = -1
#     for i in range(n):
#         max_val = max(max_val, find_maximum_path(data, i, 0))
#     print(max_val)

# 금광 다시 풀기
# 성공 (dp테이블 + 구현방식)
# t = int(input())
# for i in range(t):
#     n, m = map(int, input().split())
#     l = list(map(int, input().split()))
#     data = []
#     for i in range(0, len(l), m):
#         data.append(l[i:i+m])
#     for j in range(1, m):
#         for i in range(n):
#             if i == 0:
#                 left_up = 0
#             else:
#                 left_up = data[i-1][j-1]
#             left = data[i][j-1]
#             if i == n-1:
#                 left_down = 0
#             else:
#                 left_down = data[i+1][j-1]
#             data[i][j] = data[i][j] + max(left_up, left, left_down)
#     print(max(map(max, data)))

# Q32 정수 삼각형
# dp + 구현(점화식)방식으로 풀이 (정확히는 bottom up 방식)
# 원트 성공!!!!!! 이전문제 덕분에 한번에 풀었다
# n = int(input())
# data = []
#
# for i in range(n):
#     data.append(list(map(int, input().split())))
#
# for i in range(1, n):
#     for j in range(len(data[i])):
#         if j == 0:
#             left = 0
#         else:
#             left = data[i-1][j-1]
#         if j == len(data[i]) -1:
#             right = 0
#         else:
#             right = data[i-1][j]
#         data[i][j] = data[i][j] + max(left, right)
# print(max(map(max, data)))

# Q33 퇴사

# n = int(input())
# t = []
# p = []
# dp = [0] * (n + 1)
#
# for i in range(n):
#     a, b = map(int, input().split())
#     t.append(a)
#     p.append(b)
#
# max_val = 0
# for i in range(n-1, -1, -1):
#     time = i + t[i]
#     if time <= n:
#         dp[i] = max(p[i] + dp[time], max_val)
#         max_val = dp[i]
#     else:
#         dp[i] = max_val
# print(max_val)

# Q34 병사 배치하기
# n = int(input())
# data = list(map(int, input().split()))
#
# dp = [1] * n
#
# data.reverse()
#
# for i in range(1, n):
#     for j in range(0, i):
#         if data[i] > data[j]:
#             dp[i] = max(dp[i], dp[j] + 1)
#
# print(n-dp[n-1])

# Q35 못생긴 수
# pass
