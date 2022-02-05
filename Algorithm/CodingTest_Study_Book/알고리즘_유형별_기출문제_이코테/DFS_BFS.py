# Q15 특정 거리의 도시 찾기
# 최단경로 문제 bfs를 사용하면 쉽게 풀릴듯?
# distance 는 -1 로 초기화하는게 더 안전해보이네
# from collections import deque
# # 도시갯수, 도로의 갯수, 거리정보, 출발도시의 번호
# n, m, k, start = map(int, input().split())
#
# graph = [[] for i in range(n + 1)]
# distance = [0] * (n + 1)
# visited = [False] * (n + 1)
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#
#
# def bfs(start, graph, visited):
#     q = deque()
#     q.append(start)
#     visited[start] = True
#
#     while q:
#         now = q.popleft()
#         for i in graph[now]:
#             if not visited[i]:
#                 q.append(i)
#                 distance[i] = distance[now] + 1
#                 visited[i] = True
#
#
# bfs(start, graph, visited)
#
# count = 0
# for i in range(1, n + 1):
#     if distance[i] == k:
#         print(i)
#         count += 1
# # k 거리가 존재하지 않는 경우
# if count == 0:
#     print("-1")

# Q16 연구소
# EMPTY = 0
# WALL = 1
# VIRUS = 2
#
# n, m = map(int, input().split())
#
# data = []
# for i in range(n):
#     data.append(list(map(int, input().split())))
#
# move_type = [(-1,0),(1,0),(0,-1),(0,1)]
#
#
# def virus(data, x, y):
#     for move in move_type:
#         nx = x + move[0]
#         ny = y + move[1]
#
#         if nx >= 0 and nx < n and ny >= 0 and ny < m:
#             if data[nx][ny] == EMPTY:
#                 data[nx][ny] = VIRUS
#                 virus(data, nx, ny)
#
#
# def count_empty(data):
#     count = 0
#     for i in range(n):
#         for j in range(m):
#             if data[i][j] == EMPTY:
#                 count += 1
#     return count
#
#
# import copy
# # 벽을 3개 짓는 모든 경우의수 만들기
# def dfs(count):
#     global result
#     if count == 3:
#         temp = copy.deepcopy(data)
#         # 바이러스 퍼뜨리고
#         for i in range(n):
#             for j in range(m):
#                 if data[i][j] == VIRUS:
#                     virus(temp, i, j)
#         result = max(result, count_empty(temp))
#         return
#
#     for i in range(n):
#         for j in range(m):
#             if data[i][j] == EMPTY:
#                 data[i][j] = WALL
#                 count += 1
#                 dfs(count)
#                 data[i][j] = EMPTY
#                 count -= 1
#
# result = 0
# dfs(0)
# print(result)

# Q17 경쟁적 전염
# from collections import deque
# n, k = map(int, input().split())
#
# graph = []
# virus = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))
#     for j in range(n):
#         if graph[i][j] != 0:
#             virus.append((graph[i][j], 0, i, j))
# target_s, target_x, target_y = map(int, input().split())
#
# virus.sort()
# q = deque(virus)
#
# move_type = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# while q:
#     v, time, x, y = q.popleft()
#     if time == target_s:
#         break
#     for move in move_type:
#         nx = x + move[0]
#         ny = y + move[1]
#
#         if nx < 0 or ny < 0 or nx >= n or ny >= n:
#             continue
#         if graph[nx][ny] != 0:
#             continue
#         graph[nx][ny] = v
#         q.append((v, time + 1, nx, ny))
#
# print(graph[target_x - 1][target_y - 1])

# Q18 괄호 변환
# https://jokerldg.github.io/algorithm/2021/05/22/parentheses-change.html
# 이해하기 쉬운 코드
# def devide_str(p):
#     start_count = 0
#     end_count = 0
#     for i in range(len(p)):
#         if p[i] == '(':
#             start_count += 1
#         else:
#             end_count += 1
#         if start_count == end_count:
#             return p[:i+1], p[i+1:]
#
# def check(p):
#     stack = []
#     for word in p:
#         if word == '(':
#             stack.append('(')
#         else:
#             if not stack:
#                 return False
#             stack.pop()
#     return True
#
# def solution(p):
#     #1
#     if p == '':
#         return ''
#     #2
#     u, v = devide_str(p)
#     #3
#     if check(u):
#         return u + solution(v)
#     #4
#     else:
#         answer = '('
#         answer += solution(v)
#         answer += ')'
#         for word in u[1:len(u)-1]:
#             if word == '(':
#                 answer += ')'
#             else:
#                 answer += '('
#         return answer

# Q19 연산자 끼워 넣기

# 완전탐색 기준 시간복잠도로 계산했을 때 nCn-1 로 (수열) 2초안에 해결 가능하다 (3600만정도)
# dfs(재귀 형태로 구현), min, max 값을 찾는다
# 수열의 조합은 permu를 사용한다 (순서 따지면서)

from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
action_count = list(map(int, input().split()))

action_type = ['+', '-', '*', '/']
action = ''
for i in action_count:
    action += action_type[i] * i

permu = permutations(action, len(action))

def dfs(count):
    if count == len(permu):
        return 1e9 + 1, -1e9 - 1

    result = 0
    for i in permu:
        for j in i:
            if j == '+':
                result = numbers[j] + numbers[j+1]

