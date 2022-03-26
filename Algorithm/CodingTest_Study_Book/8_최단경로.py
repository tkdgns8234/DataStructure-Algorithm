# 최단 경로 알고리즘 종류
# 1. 다익스트라 최단 경로 알고리즘
# 2. 플로이드 워셜 알고리즘
# 3. 벨만 포드 알고리즘

# 사실 최단경로 알고리즘은 그리디 알고리즘과 다이나믹 프로그래밍 알고리즘의 한 종류


# 1. 다익스트라 최단 경로 알고리즘
# distance, graph, heap 이용함을 기억하자
# 여러개의 노드가 있을 때 특정한 노드에서 출발하여 다른노드로 가는 각각의 최단 경로를 구해주는 알고리즘
# 음의 간선이 없어야함
# 그리디 알고리즘으로 분류됨, 매번 가장 비용이 적은 노드를 선택,임의의 과정을 반복하기때문
# 간단히 구현하는 다익스트라의 경우 O(V**2) 시간복잡도 V = 노드의 수 (최단거리가 가장 짧은노드를 매번 탐색)
# 개선된 다익스트라 = O(ElogV) V는 노드의 수 E 는 간선의 수
# 개선된 다익스트라의 경우 거리가 가장 짧은노드를 탐색할 때 heap 자료구조를 이용하기 때문에 속도가 빠름
# heap 삽입, 삭제: O(logN) 

# 2. 플로이드 워셜 알고리즘
# Dab = min(Dab, Dak + Dkb) 점화식을 기억하자

# 모든 지점에서 다른 모든 지점까지의 최단경로를 모두 구하는 것
# 시간복잡도 O(n**3)
# 다이나믹 프로그래밍으로 분류 됨

#---------------다익스트라 알고리즘 #구현 쉬운버전 (O(v**2))-start

# import sys
# input = sys.stdin.readline

# #최대 거리
# INF = int(1e9)

# # 노드 수, 간선 수 입력
# n,m = map(int, input().split())
# # 시작 노드 입력
# start = int(input())
# # 최소거리
# distance = [INF] * (n+1)
# visited = [False] * (n+1)

# # 그래프 정보를 담는 리스트 생성
# graph = [[] for i in range(n + 1)]

# # 각 노드간의 정보 입력 a 에서 b 까지의 거리 = c
# for i in range(m):
#     a,b,c = map(int, input().split())
#     graph[a].append((b,c))

# def get_smallest_node():
#     smallest_distance = INF
#     index = 0
#     for i in range(1, n+1):
#         if distance[i] < smallest_distance and visited[i] is not True:
#             smallest_distance = distance[i]
#             index = i
#     return index

# def dijkstra(start):
#     # 시작노드 초기화
#     distance[start] = 0
#     visited[start] = True
#     for i in graph[start]:
#         distance[i[0]] = i[1]
#     # 시작 노드 제외한 나머지 모든 노드에 대하여
#     for i in range(n-1):
#         now = get_smallest_node()
#         visited[now] = True
#         for j in graph[now]:
#             cost = distance[now] + j[1]
#             if distance[j[0]] > cost:
#                 distance[j[0]] = cost
    
                
# dijkstra(start)
# for i in range(1, n+1):
#     if distance[i] == INF:
#         print("최소 거리를 구할 수 없습니다.")
#     else:
#         print(f"최소 거리는 {distance[i]} 입니다.")
        
#---------------다익스트라 알고리즘 #구현 쉬운버전 (O(v**2))-end
        
#---------------개선 된 다익스트라 알고리즘O(ElogV) E는 간선의 수 -start
# import heapq
# import sys
# input = sys.stdin.readline
# INF = int(1e9) # 최댓 값 지정

# # n: 노드 수, m: 간선 수 입력
# n, m = map(int, input().split())
# # 시작 노드 입력
# start = int(input())
# # 최소 거리
# distance = [INF] * (n+1)
# # 각 노드별 정보 입력을 위한 list
# graph = [[] for i in range(n+1)]

# # 노드 별 정보 입력
# for i in range(m):
#     a,b,c = map(int, input().split())
#     graph[a].append((b,c))

# #다익스트라 알고리즘
# def dijkstra(start):
#     q = []
#     # 시작 노드
#     distance[start] = 0
#     # 거리, 노드 push
#     heapq.heappush(q,(distance[start], start))
#     # queue 가 비어있을 때 까지
#     while q:
#         dis, now = heapq.heappop(q)
#         # 이미 방문한 노드는 생략
#         if distance[now] < dis:
#             continue
        
#         for i in graph[now]:
#             cost = dis + i[1]
#             if distance[i[0]] > cost:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))

# dijkstra(start)
# for i in range(1, n+1):
#     if distance[i] == INF:
#         print("거리를 알 수 없습니다.")
#     else:
#         print(distance[i])
#---------------개선 된 다익스트라 알고리즘O(ElogV) E는 간선의 수 -end

# 개선 된 다익스트라 practice
# import heapq
# import sys
# input = sys.stdin.readline
# INF = int(1e9)
#
# # 노드, 간선 수 입력
# n, m = map(int, input().split())
# # 시작노드 입력
# start = int(input())
# # 노드 정보 입력을위한 list
# graph = [[] for i in range(n+1)]
# # 최단거리
# distance =[INF] * (n+1)
#
# # 노드 정보 입력
# for i in range(m):
#     a,b,c = map(int, input().split())
#     graph[a].append((b,c))
#
# def dijkstra(start):
#     q = []
#     # 거리, 노드
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#     # queue 가 비어있지 않을 때 까지
#     while q:
#         dist, now = heapq.heappop(q)
#         # 이미 방문한 노드 생략
#         if distance[now] < dist:
#             continue
#         # 최단거리 측정
#         for i in graph[now]:
#             cost = dist + i[1]
#             if distance[i[0]] > cost:
#                 distance[i[0]] = cost
#                 heapq.heappush(q,(cost, i[0]))
#
#
# dijkstra(start)
# for i in range(1, n+1):
#     if distance[i] == INF:
#         print("출력할 수 없습니다.")
#     else:
#         print(distance[i])

# 플로이드 워셜 알고리즘
# 1. 대각선 0으로 초기화
# 2. 2차원 배열에 간선 입력
# 3. 점화식에따라 알고리즘 작성

# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# # 노드 및 간선 갯수를 입력 받기
# n = int(input())
# m = int(input())

# # graph 무한으로 초기화
# graph = [[INF for i in range(n + 1)] for i in range(n + 1)]

# for i in range(m):
#     a,b,c = map(int, input().split())
#     graph[a][b] = c

# # 대각선 0 으로 만들기
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == j:
#             graph[i][j] = 0

# for k in range(1, n+1):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# for i in range(1, n + 1):
#     for j in range(1, n+1):
#         if graph[i][j] != INF:
#             print(graph[i][j], end = " ")
#     print()

# 실전문제2 미래 도시
# bfs가 아닌 이유는 배열형태가 아니라 그래프형태 라서 그런거같은데 일단 해보자
# 전형적인 플로이드 워셜 문제였구나,, 난 이걸 다익스트라 알고리즘으로 풀었어
# 전체 회사의 갯수 N 이 100 이하라서 충분..
# O(n**3) 이면 1000000 이면 충분하네,,
# 이러면 구현이 간단한 플로이드 워셜 알고리즘으로 푸는게 더 유리하다

# import heapq
# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# n, m = map(int, input().split())

# graph = [[] for i in range(n + 1)]
# # 노드 연결 정보 초기화
# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a].append((b, 1))

# distance = [INF] * (n + 1)

# x, k = map(int, input().split())

# def dijkstra(start):
#     q = []
#     # 시작 노드 초기화
#     distance[0] = 0
#     heapq.heappush(q, (0, start))
    
#     while q:
#         dist, now = heapq.heappop(q)
#         # 이미 수행된 것은 skip
#         if distance[now] < dist:
#             continue
        
#         for i in graph[now]:
#             cost = dist + i[1]
#             if distance[i[0]] > cost:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))


# dijkstra(1)
# dist_k = distance[k]
# dijkstra(k)
# dist_x = distance[x]

# print(dist_k+dist_x)

# 실전문제2 플로이드 워셜 버전----------------------------------
# 양방향 이동 가능하다!

# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# n, m = map(int, input().split())

# graph = [[INF]*(n+1) for j in range(n + 1)]

# # 대각선 초기화
# for a in range(1, n+1):
#     for b in range(1, n+1):
#         if a == b:
#             graph[a][b] = 0

# # 노드 연결 정보 초기화
# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = 1
#     graph[b][a] = 1

# x, k = map(int, input().split())

# for k in range(1, n+1):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# print(graph[1][k] + graph[k][x])

# 실전문제3 전보
# 다익스트라 알고리즘문제같은데
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
graph = [[]for i in range(n + 1)]

for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

distance = [INF] * (n + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
        
dijkstra(start)

print(distance)

cnt = 0
max_distance = -1

for i in range(1, len(distance)):
    if distance[i] != INF:
        cnt += 1
        max_distance = max(distance[i], max_distance)

print(cnt-1, max_distance)
# 총 걸리는 시간은 하나씩 다 들렸을 때 인가?
# 도시 총 개수, 도시들이 모두 메세지를 받는데 까지 걸리는 시간이니 최대로 걸리는 사긴을 보여주면 되는구나..
# 시작지점도 제거해야해서 마지막에 cnt-1 로 출력해야해