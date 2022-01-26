# greedy 알고리즘
# 실전문제 2. 큰 수의 법칙

# n, m, k = map(int, input().split())

# l = list(map(int, input().split()))

# l.sort()

# first = l[n-1]
# second = l[n-2]

# sum = 0
# while True:
#     for i in range(k):
#         if m == 0:
#             break;
#         sum += first
#         m -= 1
#     if m != 0:
#         sum += second
#         m -= 1

# print(sum)

# 실전문제 3 숫자 카드 게임

# n, m = map(int, input().split())

# l = []
# for i in range(n):
#     row = list(map(int, input().split()))
#     row.sort()
#     l.append(row)

# result = 0
# for i in range(n):
#     result = max(result, l[i][0])

# print(result)

# 실전문제4 1이 될 때까지
# 10억 미만인 경우
# n, k = map(int, input().split())

# count = 0
# while n > 1:
#     if n % k == 0:
#         n = n // k
#         count+=1
#     else:
#         n -= 1
#         count+=1
# print(count)

# 10억 이상인 경우
# n, k = map(int, input().split())

# count = 0
# while n > 1:
#     print(n)
#     if n % k != 0:
#         a = n % k
#         if n < k:
#             a -= 1
#         n -= a
#         count += a
#     else:
#         n = n // k
#         count += 1

# print(count)

# 구현 알고리즘

# 왕실의 나이트
# 아래는 좋지못한 풀이
# 이건 그냥 -2-1, -1,-2 형식으로 이동 가능한 좌표 배열을 다 만들어놓고 이동하면 매우 간단해짐

# start = input()

# x = int(start[1])
# y = ord(start[0]) - (ord('a') - 1)

# move = ['L','R','U','D']
# move_x = [0,0,-1,1]
# move_y = [-1,1,0,0]

# pattern = ['LLU','LLD','RRU','RRD','UUL','UUR','DDL','DDR']

# rcount = 0
# count = 0
# for i in pattern:
#     rx,ry = x,y 
#     for k in i:
#         idx = move.index(k)
#         nx = rx + move_x[idx]
#         ny = ry + move_y[idx]
    
#         if nx >= 1 and ny >= 1 and nx < 9 and ny < 9:
#             rx = nx
#             ry = ny
#             count+=1
#         else:
#             break;
#         if count == 3:
#             count = 0
#             rcount += 1

# print(rcount)

# 실전문제3 게임 개발
# pass

# dfs bfs 알고리즘

# dfs 구현

# def dfs(start, visited, graph):
#     visited[start] = True
#     print(start)
    
#     for i in graph[start]:
#         if visited[i] == False:
#             dfs(i, visited, graph)    

# # 각 노드와 연결된 정보
# graph = [[],
#          [2,3,8],
#          [1, 7],
#          [1,4,5],
#          [3,5],
#          [3,4],
#          [7],
#          [2,6,8],
#          [1,7]
#          ]


# visited = [False] * len(graph)

# # 1번노드를 기준으로 dfs (깊이우선탐색 시작)
# dfs(1, visited, graph)

# bfs 구현
# from collections import deque
# def bfs(start, visited, graph):
#     visited[start] = True
#     q = deque()
#     q.append(start)
    
#     while q:
#         now = q.popleft()
#         print(now, end = " ")
#         for i in graph[now]:
#             if not visited[i]:
#                 q.append(i)
#                 visited[i] = True
        

# graph = [[],
#          [2,3,8],
#          [1, 7],
#          [1,4,5],
#          [3,5],
#          [3,4],
#          [7],
#          [2,6,8],
#          [1,7]
#          ]

# visited = [False] * len(graph)

# bfs(1, visited, graph)

# 실전문제 3 음료수 얼려먹기
# bfs나 dfs 나 둘 다 구현할 수 있을거같다 다만, 탐색이 모두 완료된 후 결과를 도출해야하기때문에
# 스택 형태의 자료구조가 좋을거라 판단하여 dfs 를 선택했다

# def dfs(x, y, graph):
#     if x < 0 or y < 0 or x >= n or y >= m:
#         return False
#     if graph[x][y] == 0:
#         graph[x][y] = 1
        
#         dfs(x-1, y, graph)
#         dfs(x+1, y, graph)
#         dfs(x, y-1, graph)
#         dfs(x, y+1, graph)
#         return True
#     return False
    
# n, m = map(int, input().split())

# graph = []
# # ---------------------------
# # 잘못됐다.. 파이썬은 string을 list 형변환 하기만 해도 하나씩 잘려서 들어간다
# # for i in range(n):
# #     a = input()
# #     l = []
# #     for word in a:
# #         l.append(int(word))
# #     graph.append(l)
# # ---------------------------
# for i in range(n):
#     graph.append(list(map(int, input())))

# # 0 은 움직일 수 있는곳 1 은 안되는 곳

# count = 0
# # visited 필요없을듯? 1로 바꾸면 되니까
# for i in range(n):
#     for j in range(m):
#         if dfs(i,j,graph) == True:
#             count += 1

# print(count)

# 실전문제 4 미로탈출
# 최단거리 bfs 이용
# from collections import deque
# n, m = map(int, input().split())

# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

# move = ['L','R','U','D']
# move_x = [0, 0, -1, 1]
# move_y = [-1, 1, 0, 0]
# # bfs 구현
# x, y = 0, 0
# q = deque()
# q.append((0,0))

# while q:
#     x, y = q.popleft()
        
#     for i in range(len(move)):
#         nx = x + move_x[i]
#         ny = y + move_y[i]
#         if nx < 0 or ny < 0 or nx >= n or ny >= m:
#             continue
#         if graph[nx][ny] == 0:
#             continue
#         if graph[nx][ny] == 1:
#             graph[nx][ny] = graph[x][y] + 1
#             q.append((nx,ny))
    
#     if graph[n-1][m-1] != 1:
#         print(graph[nx][ny])
#         break;

# 정렬 알고리즘
# 버블 정렬
# arr = [1,3,2,3,52,67,5,2,4]

# n = len(arr)
# for i in range(n):
#     for j in range(n-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]

# print(arr)

# 선택 정렬
# 가장 작은 원소를 맨 앞부터 선택하여 배치시키는 정렬법 O(n^2)
# arr = [1,3,2,3,52,67,5,2,4]

# for i in range(len(arr)):
#     min_index = i
#     for j in range(i+1,len(arr)):
#         if arr[min_index] > arr[j]:
#             min_index = j
#     arr[min_index], arr[i] = arr[i], arr[min_index]

# print(arr)

# 삽입 정렬
# 1번째 원소부터 삽입하며 정렬하는 방식

# arr = [1,2,3,31,4,21,313,2]

# for i in range(1, len(arr)):
#     for j in range(i,0,-1):
#         if arr[j] < arr[j-1]:
#             arr[j], arr[j-1] = arr[j-1], arr[j]
#         else:
#             break;
# print(arr)

# 퀵 정렬
# 피벗을 이용한 정렬 방법 nLogn 시간 소요

# arr = [1,2,31,4,21,421,43,2,1]

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[0]
#     tail = arr[1:]
    
#     left_side = [i for i in tail if i <= pivot]
#     right_side = [i for i in tail if i > pivot]
    
#     return quick_sort(left_side) + [pivot] + quick_sort(right_side)

# arr = quick_sort(arr)
# print(arr)

# 계수 정렬
# 배열에 숫자를 모두 저장 후 출력

# arr = [12,3,14,31,4,12,31,3,1,21,4312,34,12]

# count = [0] * (max(arr)+1)

# for i in arr:
#     count[i] += 1

# for i in range(len(count)):
#     for j in range(count[i]):
#         print(i,end=" ")