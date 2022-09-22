from collections import deque

INF = int(1e9)
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [INF] * (N + 1)


def dijkstra():
    q = deque([1])
    dist[1] = 0

    while q:
        now = q.popleft()
        for i in graph[now]:
            if dist[i] > dist[now] + 1:
                dist[i] = dist[now] + 1
                q.append(i)


dijkstra()

max_dist = -1
for i in range(1, N + 1):
    if dist[i] != INF:
        max_dist = max(max_dist, dist[i])

dist_cnt = dist.count(max_dist)
first_index = dist.index(max_dist)

print(first_index, max_dist, dist_cnt)
