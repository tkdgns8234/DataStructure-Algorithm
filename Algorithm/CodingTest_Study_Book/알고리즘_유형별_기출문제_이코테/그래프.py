# Q41 여행 계획
# 전형적인 union-find 문제 (집합 관계 판별)
# n, m = map(int, input().split())
#
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
#
# def union_find(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#
#     if a > b:
#         parent[a] = b
#     else:
#         parent[b] = a
#
#
# parent = [[] for i in range(n + 1)]
#
# for i in range(n + 1):
#     parent[i] = i
#
# data = []
# for i in range(n):
#     data.append(list(map(int, input().split())))
#
# for i in range(5):
#     for j in range(5):
#         if data[i][j] == 1:
#             union_find(parent, i, j)
#
#
# result = True
# trip = set(map(int, input().split()))
# val = parent[list(trip)[0]]
# for i in trip:
#     if parent[i] != val:
#         result = False
#
# print("YES" if result else "NO")

# Q42 탑승구
# 풀이 방식이 정말 신기하네
# 다시 풀어보자

# Q43 어두운 길
# 전형적인 크루스칼 알고리즘 어려울게 없다
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
#
# def union_find(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#
#     if a > b:
#         parent[a] = b
#     else:
#         parent[b] = a
#
#
# n, m = map(int, input().split())
#
# edges = []
# parent = [[] for i in range(n + 1)]
# for i in range(n + 1):
#     parent[i] = i
#
# for i in range(m):
#     x, y, dist = map(int, input().split())
#     edges.append((dist, x, y))
#
# edges.sort()
#
# total = 0
# result = 0
# for edge in edges:
#     dist, x, y = edge
#     total += dist
#     if find_parent(parent, x) != find_parent(parent, y):
#         result += dist
#         union_find(parent, x, y)
#
# print(total - result)

# Q44 행성 터널
# 다시풀자, 실패
# 아이디어는 90% 맞았다 좀 더 했으면 풀었을듯?
# n = int(input())
#
# pos = []
# for i in range(n):
#     x, y, z = map(int, input().split())
#     pos.append((x, y, z))
# pos.sort()
#
# edges = []
# for i in range(len(pos) - 1):
#     x, y, z = pos[i]
#     nx, ny, nz = pos[i + 1]
#     dist = min(x-nx, y-ny, z-nz)
#
#     edges.append((dist, ))