# 다익스트라 기본 문제
import heapq
INF = int(1e9)

def solution(n, edge):
    distance = [INF] * (n+1)
    graph = [[] for _ in range(n+1)]

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    def dijkstra(start):
        q = []
        distance[start] = 0
        heapq.heappush(q, (1, 0))
        while q:
            now, dist = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                if distance[i] > dist + 1: # 모든 이동 거리는 1
                    distance[i] = dist + 1
                    heapq.heappush(q, (i, distance[i]))

    dijkstra(1)
    return distance.count(max([i for i in distance if i != INF]))


v = solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
print(v)