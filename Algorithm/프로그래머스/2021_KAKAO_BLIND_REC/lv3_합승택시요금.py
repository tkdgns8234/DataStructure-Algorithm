# 최단거리 문제인데
# 둘 다 끝까지 같이 타는게 아니라
# 도중에 한명은 내리기도하고
# 또 따로타기도 하네?
# 미치겠다. 모르겠어

# 프로그래머스 풀이 보니까 허무하다..
# 아이디어만 떠올리면 간단해보이네
# 사실 문제에 답이 나와있다.
# 일반적인 다익스트라, 플로이드 와샬 알고리즘으로 모든 최단경로를 갱신한 후에
# 문제에 주어진 대로 점화식을 짜면 된다
# answer = min(dist[s][k] + dist[k][b] + dist[k][a])



# 플로이드-와샬 버전
# INF = int(1e9)
# def solution(n, s, a, b, fares):
#     dist = [[INF] *(n+1) for _ in range(n+1)]
#
#     for i, j, c in fares:
#         dist[i][j] = c
#         dist[j][i] = c
#
#     for k in range(1, n+1):
#         for i in range(1, n+1):
#             for j in range(1, n + 1):
#                 if i == j:
#                     dist[i][j] = 0
#                 else:
#                     dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
#     answer = INF
#     for k in range(1, n+1):
#         answer = min(answer, dist[s][k] + dist[k][a] + dist[k][b])
#     return answer
#
# v = solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]	 )
# print(v)



# 다익스트라 버전
import heapq

INF = int(1e9)
def solution(n, s, a, b, fares):
    distance = [[INF] * (n+1) for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    for i, j, c in fares:
        graph[i].append((j, c))
        graph[j].append((i, c))

    def dijkstra(i):
        distance[i][i] = 0
        q = []
        heapq.heappush(q, (0, i))

        while q:
            cost, now = heapq.heappop(q)
            if distance[i][now] < cost:
                continue

            for nn, nc in graph[now]:
                if distance[i][nn] > cost + nc:
                    distance[i][nn] = cost + nc
                    heapq.heappush(q, (cost + nc, nn))

    for i in range(1, n+1):
        dijkstra(i)

    answer = INF
    for k in range(1, n+1):
        answer = min(answer, distance[s][k] + distance[k][a] + distance[k][b])
    return answer


v = solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]	 )
print(v)