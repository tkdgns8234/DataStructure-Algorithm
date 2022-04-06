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
#             if not 0 <= nx < MAX:
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