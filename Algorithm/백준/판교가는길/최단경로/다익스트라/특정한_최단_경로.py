# v1, v2 를 거치는 방법
# 1. start - v1 - v2 - end
# 2. start - v2 - v1 - end
# 각각의 최단거리를 구한다

import heapq
INF = int(1e9)
V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

V1, V2 = map(int, input().split())

def dijkstra(start, end):
    distance = [INF] * (V + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        # 방향성이 없어도 최단거리가 아닌경우 아래에서 걸러진다.
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = i[1] + dist
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance[end]

# 1. start - v1 - v2 - end
ans1 = dijkstra(1, V1) + dijkstra(V1, V2) + dijkstra(V2, V)

# 2. start - v2 - v1 - end
ans2 = dijkstra(1, V2) + dijkstra(V2, V1) + dijkstra(V1, V)

ans = min(ans1, ans2)

if ans >= INF:
    print(-1)
else:
    print(ans)