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

# 첫 번째 생각한 풀이 방법
# 완전탐색 기준 시간복잠도로 계산했을 때 nPn-1 로 (수열) 2초안에 해결 가능하다 (3600만정도)
# dfs(재귀 형태로 구현), min, max 값을 찾는다
# 수열의 조합은 permu를 사용한다 (순서 따지면서)

# ------------------
# 잘못생각했네
# 문제에 대한 풀이는 2가지로 나뉜다
# 1. dfs를 이용해서 완전탐색을 수행하는 방법
# 2. 순열을 이용해서 반복문을 통해 완전탐색을 수행하는 방법
# 두가지 방법 다 풀어보자 (현재 재귀 구현이 약한거같다)
# 순열 중 permutations 를 이용하는 방법의 경우 중복되는 경우가 많기때문에 set 자료형을 사용

# 1. 순열을 이용하는 방법
# from itertools import permutations
#
# n = int(input()) # 수의 갯수
# num = list(map(int, input().split()))
# oper = list(map(int, input().split()))
# oper_type =['+','-','*','/']
#
# op = []
# for i in range(4):
#     for j in range(oper[i]):
#         op.append(oper_type[i])
#
# def solve():
#     min_val = 1e9
#     max_val = -1e9
#
#     for case in set(permutations(op, n-1)):
#         result = num[0]
#         for i in range(len(case)):
#             if case[i] == "+":
#                 result += num[i + 1]
#             elif case[i] == "-":
#                 result -= num[i + 1]
#             elif case[i] == "*":
#                 result *= num[i + 1]
#             elif case[i] == "/":
#                 result = int(result / num[i + 1])
#         max_val = max(max_val, result)
#         min_val = min(min_val, result)
#
#     return min_val, max_val
#
# min, max = solve()
# print(min)
# print(max)

# 2. dfs를 이용하는 방법
# DFS 재귀 구현 팁
# 1. 종료 조건을 어떻게 설정할 것인지
# 2. 함수 호출에따라 어떤 값이 지속적으로 바뀌는지 ( 바뀌는 값을 매개변수로 재귀적 전달 )
# n = int(input()) # 수의 갯수
# num = list(map(int, input().split()))
# add, minus, mul, dev = list(map(int, input().split()))
#
# min_val = 1e9
# max_val = -1e9
#
# def dfs(op_count, val, add, minus, mul, dev):
#     global min_val, max_val
#     if op_count == n-1:
#         min_val = min(val, min_val)
#         max_val = max(val, max_val)
#         return
#
#     # elif 가 아닌 if 문이기때문에 완전탐색 가능
#     if add > 0:
#         dfs(op_count + 1, val + num[op_count+1], add - 1, minus, mul, dev)
#     if minus > 0:
#         dfs(op_count + 1, val - num[op_count+1], add, minus - 1, mul, dev)
#     if mul > 0:
#         dfs(op_count + 1, val * num[op_count+1], add, minus, mul - 1, dev)
#     if dev > 0:
#         dfs(op_count + 1, int(-(-val / num[op_count+1])) if val < 0 else val//num[op_count+1], add, minus, mul, dev-1)
#         #dfs(op_count + 1, int(val / num[op_count+1]), add, minus, mul, dev - 1) # 두가지 방법 모두 가능
#
# dfs(0, num[0], add, minus, mul, dev)
# print(min_val)
# print(max_val)

# Q20 감시 피하기
# 풀긴했는데 조금 아쉽다

# n = int(input())
# data = []
# for _ in range(n):
#     data.append(list(input().split()))
#
# move_type = [(-1,0), (1, 0), (0, -1), (0, 1)]
# result = False
#
# def confirm(fx, fy):
#     for move in move_type:
#         x = fx
#         y = fy
#         while True:
#             nx = x + move[0]
#             ny = y + move[1]
#
#             if nx < 0 or ny < 0 or nx >= n or ny >= n:
#                 break
#             if data[nx][ny] == 'O':
#                 break
#             if data[nx][ny] == 'S':
#                 return False
#             x = nx
#             y = ny
#     return True
#
# def dfs(count):
#     global result
#     if count == 3:
#         for r in range(n):
#             for c in range(n):
#                 if data[r][c] == 'T':
#                     if not confirm(r, c):
#                         return
#
#         result = True
#         return
#     for i in range(n):
#         for j in range(n):
#             if data[i][j] == 'X':
#                 data[i][j] = 'O'
#                 dfs(count + 1)
#                 data[i][j] = 'X'
#
# dfs(0)
# print("YES" if result else "NO")


# Q21 인구 이동
# 아래는 틀린 풀이 밑에 다시 푼 버전이 있다
# bfs 로 풀면 O(n^2) 로 풀 수 있다
# bfs 를 모든 배열 위치에서 실행햐아한다
# 이유 1 국가 연합이 한 칸 이상 떨어져 존재할 수 있다
# 2. bfs 를 q로 구현할 때 인접국가인 경우에만 q에 추가하여 추가 탐색을 시도하기 때문에
# start 로 주어진 위치만 탐색하고 끝날 수도 있다

# from collections import deque
# N, L, R = map(int, input().split())
#
# data = []
# for _ in range(N):
#     data.append(list(map(int, input().split())))
#
# move_type = [(1, 0), (-1, 0), (0, -1),  (0, 1)]
#
# def bfs():
#     q = deque()
#     count = 0
#     need_change = True
#     while need_change:
#         q.append((0, 0))
#         change = []
#         visited = [[False] * N for i in range(N)]
#         while q:
#             x, y = q.popleft()
#             for move in move_type:
#                 nx = x + move[0]
#                 ny = y + move[1]
#
#                 if nx < 0 or ny < 0 or nx >= N or ny >= N:
#                     continue
#                 if not visited[nx][ny]:
#                     if L <= abs(data[nx][ny] - data[x][y]) <= R:
#                         change.append((nx, ny))
#                         change.append((x, y))
#                         visited[nx][ny] = True
#                     q.append((nx, ny))
#
#         change = set(change)
#         sum = 0
#         for x, y in change:
#             sum += data[x][y]
#         for x, y in change:
#             data[x][y] = sum // len(change)
#         print(data)
#
#         if len(change) > 0:
#             need_change = True
#             count += 1
#         else:
#             need_change = False
#     return count
#
# result = bfs()
# print(result)

# import sys
# import math
# from collections import deque
#
# # 남 동 북 서
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
#
# n, l, r = map(int, sys.stdin.readline().split())  # n*n, 인구차이 l명 이상, r명 이하
#
# arr = list()
# a_list = list()
# for i in range(n):
#     arr.append(list(map(int, sys.stdin.readline().split())))
#
# def bfs(i, j):
#     dq = deque()
#     dq.append((i, j))
#     visit[i][j] = True
#     # 연합된 국가 담기
#     union = [(i, j)]
#     count = arr[i][j]   # 총 연합된 국가 수
#         # 1. 인접 국가를 탐색하면서 인구차이 l명 이상, r명 이하인 경우 연합 국가에 담기
#     while dq:
#         x, y = dq.popleft()
#         for d in range(4):
#             nx = x + dx[d]
#             ny = y + dy[d]
#             if nx < 0 or ny < 0 or nx >= n or ny >= n:
#                 continue
#             if visit[nx][ny]:
#                 continue
#             if l <= abs(arr[nx][ny] - arr[x][y]) <= r:  # 인구차이 l명 이상, r명 이하인 경우, 연합 국가에 담기
#                 union.append((nx, ny))
#                 visit[nx][ny] = True
#                 dq.append((nx, ny))
#                 count += arr[nx][ny]
#     # 2. 연합 국가 간 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수) 가 되도록 계산
#     for x, y in union:
#         arr[x][y] = math.floor(count / len(union))
#     return len(union)
#
# result = 0    # 인구 이동이 발생하는 일수
# while True:   # 1. 인구 이동이 없을 때까지 반복
#     visit = [[False] * n for _ in range(n)]
#     flag = False  # 인구 이동 존재 유무 플래그
#     # 2. 모든 곳을 bfs로 방문하여 연합 진행
#     for i in range(n):
#         for j in range(n):
#             if not visit[i][j]:
#                 if bfs(i, j) > 1:
#                     flag = True
#     if not flag:   # 3. 지금까지 인구 이동이 없는 경우, 그만
#         break
#     result += 1
#
# print(result)


# Q21 인구 이동 재풀이
# import math
# from collections import deque
# n, l, r = map(int, input().split())
#
# data = []
#
# for i in range(n):
#     data.append(list(map(int, input().split())))
#
# move_type = [(1, 0), (-1, 0), (0, -1), (0, 1)] # 상하좌우
# def dfs(x, y):
#     q = deque()
#     q.append((x, y))
#     visited[x][y] = True
#     union = []
#     union_person_cnt = []
#     union.append((x, y))
#     union_person_cnt.append(data[x][y])
#
#     while q:
#         x, y = q.popleft()
#         for move in move_type:
#             nx = x + move[0]
#             ny = y + move[1]
#
#             if nx < 0 or ny < 0 or nx >= n or ny >= n:
#                 continue
#             if visited[nx][ny]:
#                 continue
#             if l <= abs(data[x][y] - data[nx][ny]) <= r:
#                 q.append((nx, ny))
#                 union.append((nx, ny))
#                 union_person_cnt.append(data[nx][ny])
#                 visited[nx][ny] = True # 놓쳤었다.. 실수하지 말자 bfs 계속 풀어봐야할듯
#
#     for x, y in union:
#         data[x][y] = math.floor(sum(union_person_cnt) / len(union))
#     print(data)
#     return True if len(union) > 1 else False
#
#
# # 연합국이 존재하는지 확인하기 위한 flag
# count = 0
# while True:
#     visited = [[False] * n for i in range(n)]
#     flag = False
#     for i in range(n):
#         for j in range(n):
#             if not visited[i][j]: # 이게 없어서 매우 애먹었다.. 자꾸 하나씩 빠뜨리지 말자
#                 if dfs(i, j):
#                     flag = True
#     # 연합국이 존재하는 경우
#     if flag:
#         count += 1
#     # 연합국이 존재하지 않는경우
#     else:
#         break
# print(count)

# Q22 블록 이동하기
# 아래에서 멈춤.. 풀이 보고 다시풀어보자
# bfs + 구현 문제

# from collections import deque
# move_type = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#
# def bfs(board):
#     n = len(board)
#     start = (0, (0, 0), (0, 1))
#     target = (n, n)
#     q = deque()
#     q.append(start)
#
#     while q:
#         distance, a, b = q.popleft()
#         for move in move_type:
#             nxa = a[0] + move[0]
#             nya = a[1] + move[1]
#             nxb = b[0] + move[0]
#             nyb = b[1] + move[1]
#
#             if nxa < 0 or nya < 0 or nxb < 0 or nyb < 0 or nxa >= n or nya >= n or nxb >= n or nyb >= n:
#                 continue
#             if nxa == -1 or nya == -1 or nxb == -1 or nyb == -1:
#                 continue
#
#             q.append(distance + 1, (nxa, nya), (nxb, nyb))
#
#             board[nxa][nya] = min(board[nxa][nya], distance + 1)
#             board[nxb][nyb] = min(board[nxa][nya], distance + 1)
#
#
# def solution(board):
#     answer = 0
#     # 벽을 -1로 초기화
#     n = len(board)
#     for i in range(n):
#         for j in range(n):
#             if board[i][j] == 1:
#                 board[i][j] = -1
#
#     bfs(board)
#     answer = board[n - 1][n - 1]
#     return answer


# Q22 블록 이동하기
