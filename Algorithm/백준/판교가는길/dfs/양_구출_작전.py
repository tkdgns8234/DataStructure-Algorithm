# dp 형식을 같이 써야하나
# 아래는 실패한 코드
# 늑대는 최대 1마리 양을 먹을 수 있다는 특징을 보지못했다.

# N = int(input())
# dp = [0] * (N + 1)
# data = []
# for i in range(N-1):
#     data.append(list(input().split()) + [i+2])
#
# for animal, count, move, index in sorted(data, key=lambda x: x[2]):
#     if animal == 'W':
#         dp[index] = dp[int(move)] + int(count)
#     else:
#         dp[index] = dp[int(move)]
#
# ans = 0
# for animal, count, move, index in data:
#     if animal == 'S':
#         diff = int(count) - dp[int(move)]
#         ans += diff if diff >= 0 else 0
# print(ans)

# 완전탐색 O(n^2)로 실패

# N = int(input())
# data = []
# for i in range(N-1):
#     data.append(list(input().split()))
#
# result = 0
# now = 0
# for animal, count, move in data:
#     if animal == 'S':
#         now = int(count)
#         move = int(move)
#         while True:
#             if move-2 == -1:
#                 break
#             if data[move-2][0] == 'W':
#                 diff = now - int(data[move-2][1])
#                 now = diff if diff > 0 else 0
#
#             if move == int(data[move-2][2]): # 1까지 도달 불가
#                 break
#             move = int(data[move-2][2])
#
#         result += now
# print(result)



# 5
# S 10 1
# S 100 2
# W 50 1
# S 10 1

# dfs를 통해 리프노드까지 내려가서
# 양이 몇마리 올라오는지 체크하는 방식
# 경로는 유일하다 라는 말이 있기에 트리방식을 유추하고 아래같은 방식으로 해결할 수 있다

# 리프노드에서 올라오면서 모든 양을 더하므로 섬을 탐색하는데 걸리는 경우의 수가 줄어듦
# dfs를 사용한 방식
# 늑대는 최대 1마리 양을 먹을 수 있음에 유의!!!
#
# import sys
# sys.setrecursionlimit(int(1e7))
#
# input = sys.stdin.readline
# N = int(input())
# data = [[0, []] for _ in range(N + 1)]
# for i in range(2, N + 1):
#     animal, count, move = input().split()
#     count = int(count)
#     move = int(move)
#     if animal == 'W': count = -count
#     data[i][0] = count
#     data[move][1].append(i)
#
# def dfs(s):
#     v = data[s][0]
#     for i in data[s][1]:
#         v += dfs(i)
#     if v < 0:
#         v = 0
#     return v
#
# ans = dfs(1)
# print(ans)

# 위상 정렬을 이용한 방식
# import sys
# from collections import deque
# input = sys.stdin.readline
#
# N = int(input())
# in_degree = [0] * (N+1)
# data = [[0, 0] for _ in range(N+1)]
#
# for i in range(2, N + 1):
#     animal, count, move = input().split()
#     count, move = int(count), int(move)
#     if animal == 'W': count = -count
#     data[i][1] = move
#     data[i][0] = count
#     in_degree[move] += 1
#
# def topology():
#     q = deque()
#     for i in range(2, N+1):
#         if in_degree[i] == 0:
#             q.append(i)
#
#     while q:
#         now = q.popleft()
#         now_v = data[now][0]
#         parent = data[now][1]
#
#         if now_v > 0:
#             data[parent][0] += now_v
#
#         in_degree[parent] -= 1
#         if in_degree[parent] == 0:
#             q.append(parent)
#
# topology()
# print(data[1][0])


