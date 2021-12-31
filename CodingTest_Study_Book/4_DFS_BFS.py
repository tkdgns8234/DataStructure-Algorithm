# DFS : Depth first search 깊이우선탐색
# BFS : Breadth first search 너비우선탐색
# 트리, 그래프 탐색을 위한 대표적인 두 가지 알고리즘

# 자료구조: 데이터를 표현, 관리, 처리하기위한 구조
#스택
# l = list()
# l.append(0)
# l.append(1)
# l.pop()
# print(l)

# 큐
# deque가 양방향 큐 , 파이썬의 list가 단방향 큐 라고 생각하면 된다. 단, 파이썬의 list는 오른쪽을 기준으로하기에 왼쪽 요소 삽입,삭제 시 O(N)시간소요될수있다.
# 그래서 deque 를 사용한다. (양방향큐) 
# from collections import deque
# queue = deque()
# queue.append(1)
# queue.append(1)
# queue.popleft()
# print(list(queue))

# 재귀 함수
# 재귀 함수는 내부적으로 메인 메모리의 스택공간에 적재됨 이 말인 즉, 스택구현과 관련된 문제를 재귀로 해결할경우 효과적임
# 재귀의 경우 수학에서의 점화식 (특정한 함수를 자신보다 더 작은 변수에 대한 함수와의 관계로 표현)표현을 그대로 소스코드로 옯겼기때문에
# 비교적 더 간단하게 표현할 수 있다.

# 재귀 작성 요령
# def recursive():
#    if 종료조건
#    return
#    점화식

#DFS
# 그래프에서 깊은곳을 우선적으로 탐색하는 알고리즘
# 스택, 재귀함수이용 구현
# 그래프 표현 방법
# 1. 인접 행렬: 2차원 배열로 그래프의 연결 관계를 표현
# 2. 인접 리스트: 리스트로 그래프의 연결 관계 표현

# BFS
# 그래프에서 가까운 노드부터 탐색
# 큐, deque 자료구조 이용 구현

# 모든노드 방문- > 둘 다 비슷함
# 경로의 특징 을 저장해야하는문제 dfs 사용
# 미로찾기, 최단경로 -> bfs 사용

# 일반적으로 그래프의 크기가 엄청나게 큰것이아니면 bfs가 효율이 더 좋다


# ## DFS 로 완전탐색 구현
# # 스택 -> 재귀함수이용 구현한다고 생각하고 시작

# def dfs(graph, start, visited):
#     visited[start] = True
#     print(start, end=" ")
#     for i in graph[start]:
#         if not visited[i]:
#             dfs(graph, i, visited)
#     return
# # 책 137page 참고
# graph = [
#     # 요소가 1부터라 첫 번째 행은 비운다
#     [],
#     [2,3,8],
#     [1,7,],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]

# visited = [False] * len(graph)

# dfs(graph, 1, visited)


# ## BFS 로 완전탐색 구현
# # 큐, deque 자료구조 이용 구현한다고 생각
# from collections import deque

# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         v = queue.popleft()
#         print(v, end = " ")
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
                
# graph = [
#     # 요소가 1부터라 첫 번째 행은 비운다
#     [],
#     [2,3,8],
#     [1,7,],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]

# visited = [False] * len(graph)

# bfs(graph, 1, visited)

## 실전문제 3 음료수 얼려 먹기

n, m = map(int, input().split())

ice = [[[0]* m] for _ in range(n)]

blocked = [False] * len(ice)

# dfs, bfs 문제는 일단 어떤알고리즘을 적용해야하는지 파악하는게 가장 중요하네
# 어렵다.. 내일 다시 풀자