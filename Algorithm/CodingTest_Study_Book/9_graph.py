# 그래프 알고리즘
# 알고리즘 문제를 접했을 때 '서로다른 개체가 연결되어있다' 는 표현이 있을 시, 그래프 알고리즘을 떠올려라
# 그래프와 트리는 엄연히 다르다
# 다익스트라 알고리즘 (우선순위 큐 사용)의 경우 인접 리스트 방식
# 플로이드 워셜 알고리즘의 경우 인접 행렬 방식

# 인접 리스트와 인접 행렬방식의 경우 메모리와 속도측면의 차이가 있다( 설명은 생략 )

# 1. Union-find 알고리즘( 서로소 알고리즘 )
# 주로 두 집합이 서로소 관계인지 판별하거나
# 사이클을 판별할 때 사용한다 (사이클 판별의 경우 무방향 그래프에서만 가능하다.)
# 사이클: 특정 정점을 지나 다시 처음 정점(노드) 로 돌아오는 경우가 존재하는경우 사이클 발생

# 1-1. 서로소를 통해 집합 판별
# find_parent 의 return 이 x가 아니라 parent[x] 여야함
# 정보출력시 find_parent()로 호출하도록 하자

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
    
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# v, e = map(int, input().split())

# parent = [0] * (v + 1)

# # 각 노드의 부모를 자기 자신으로 초기화
# for i in range(1, v+1):
#     parent[i] = i

# # 간선의 수 만큼 반복 입력, union 작업 호출
# for i in range(e):
#     a, b = map(int, input().split())
#     union(parent, a, b)

# # 부모정보 출력
# for i in range(1, v+1):
#     print(find_parent(parent,i), end = " ")

# 1-2. 서로소를 통해 사이클 확인
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_find(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a > b:
#         parent[a] = b
#     else:
#         parent[b] = a

# v, e = map(int, input().split())

# parent = [0] * (v + 1)

# for i in range(1, v+1):
#     parent[i] = i
    
# cycle = False

# for _ in range(e):
#     a, b = map(int, input().split())
#     if find_parent(parent, a) == find_parent(parent, b):
#         cycle = True
#         break
#     else:
#         union_find(parent, a, b)
# if cycle:
#     print("사이클 발생")
# else:
#     print("사이클 미 발생")

# 2. 신장 트리
# 하나의 그래프가 있을 때 노드 간의 사이클이 존재하지 않고 모든 노드를 포함하는경우(끊어진 노드가 없는 경우) 신장 트리 라고 한다.
# 최소 신장 트리 알고리즘 (ex) a, b 도로 연결 시 최소한의 비용) 굳이 세개의 간선으로 연결할 필요는 없다
# 대표적인 최소 신장 트리 알고리즘으로는 크루스칼 알고리즘이 있다.

# 크루스칼 알고리즘: 가장 적은 비용으로 모든 노드를 연결할 수 있다. 
# 그리디 알고리즘으로 분류됨
# 1. 모든 간선에 대해 정렬을 수행한 뒤에 
# 2. 거리가 가장 짧은 순서대로 집합에 포함시킨다.
# 3. 이 때 사이클이 발생할 수 있는경우 생략한다.
# 크루스칼 알고리즘의경우 간선의 갯수가 E 일 때 ElogE의 시간복잡도를 가진다.
# 왜냐하면 크루스칼 알고리즘에서 가장 큰 작업은 정렬이며, 정렬의경우 LogE 의 시간복잡도를 가지기 때문이다.

# 2-1 짧은 거리 연결 최소신장트리
# import sys
# input = sys.stdin.readline

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_find(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a>b:
#         parent[a] = b
#     else:
#         parent[b] = a

# v, e = map(int, input().split())

# parent = [0] * (v + 1)

# for i in range(v + 1):
#     parent[i] = i

# sum = 0
# edges = []

# for _ in range(e):
#     a, b, cost = map(int, input().split())
#     edges.append((cost, a, b))
    
# edges.sort()

# for edge in edges:
#     cost, a, b = edge 
#     if find_parent(parent, a) != find_parent(parent, b):
#         sum += cost
#         union_find(parent, a, b)

# print(sum)


# 3. topology sort 위상 정렬
# 순서가 정해진 일련의 작업을 차례대로 수행해야할 때 사용
# 진입 차수가 0 인것을 지속적으로 찾으면서 정렬 하는 방법
# from collections import deque

# v, e = map(int, input().split())

# indegree = [0] * (v + 1)
# graph = [[]for i in range(v + 1)]

# for i in range(e):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     indegree[b] += 1

# def topologysort():
#     result = []
#     q = deque()
#     for i in range(1, v + 1):
#         if indegree[i] == 0:
#             q.append(i)
    
#     while q:
#         now = q.popleft()
#         result.append(now)
#         for i in graph[now]:
#             indegree[i] -= 1
#             if indegree[i] == 0:
#                 q.append(i)
    
#     for i in result:
#         print(i, end=" ")
        
# topologysort()

# 실전문제2 팀 결성
