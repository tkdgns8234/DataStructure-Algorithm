# Q37 플로이드
# INF = int(1e9)
# n = int(input())
# m = int(input())
# graph = [[INF] * (n + 1) for i in range(n + 1)]
#
# for _ in range(m):
#     a, b, cost = map(int, input().split())
#     if graph[a][b] > cost:
#         graph[a][b] = cost
#
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == j:
#             graph[i][j] = 0
#
# for k in range(1, n + 1):
#     for a in range(1, n + 1):
#         for b in range(1, n + 1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
#
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if graph[i][j] != INF:
#             print(graph[i][j], end=" ")
#     print()

# Q38 정확한 순위
# 다시풀자

# Q39 화성 탐사
# 가중치가 존재하니 bfs가 아닌 다익스트라 알고리즘으로 해결해야한다
# import heapq
# INF = int(1e9)
# move_type = [(1, 0), (-1, 0), (0, -1), (0, 1)]
# test_case = int(input())
# for case in range(test_case):
#     n = int(input())
#     distance = [[INF] * (n + 1) for i in range(n + 1)]
#
#     graph = []
#     for _ in range(n):
#         graph.append(list(map(int, input().split())))
#
#     q = []
#     heapq.heappush(q, (graph[0][0], 0, 0))
#     distance[0][0] = graph[0][0]
#
#     while q:
#         dist, x, y = heapq.heappop(q)
#
#         if dist > distance[x][y]:
#             continue
#
#         for move in move_type:
#             nx = x + move[0]
#             ny = y + move[1]
#
#             if nx < 0 or ny < 0 or nx >= n or ny >= n:
#                 continue
#             cost = dist + graph[nx][ny]
#             if distance[nx][ny] > cost:
#                 distance[nx][ny] = cost
#                 heapq.heappush(q, (cost, nx, ny))
#
#     print(distance[n-1][n-1])

# Q40 숨바꼭질
# import heapq
# INF = int(1e9)
# n, m = map(int, input().split())
#
# graph = [[] for i in range(n + 1)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append((b, 1))
#     graph[b].append((a, 1))
#
# distance = [INF] * (n + 1)
#
# q = []
# start = 1
# heapq.heappush(q, (0, start))  #start => 1
# distance[start] = 0
#
# while q:
#     dist, now = heapq.heappop(q)
#     if distance[now] < dist:
#         continue
#
#     for i in graph[now]:
#         cost = dist + i[1]
#         if distance[i[0]] > cost:
#             distance[i[0]] = cost
#             heapq.heappush(q, (cost, i[0]))
#
# index = 0
# maximum = 0
#
# for i in range(1, n + 1):
#     if distance[i] != INF:
#         if maximum < distance[i]:
#             maximum = distance[i]
#             index = i
#
# print(index, maximum, distance.count(maximum))
