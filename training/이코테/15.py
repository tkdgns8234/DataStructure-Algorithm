from collections import deque

INF = int(1e9)


def bfs():
    global dist
    q = deque()
    q.append(X)
    dist[X] = 0

    while q:
        now = q.popleft()

        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                dist[i] = dist[now] + 1
                visited[i] = True


N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

visited = [False] * (N + 1)
dist = [INF] * (N + 1)

bfs()

result = []
for idx, d in enumerate(dist):
    if d == K:
        result.append(idx)

if len(result) > 0:
    print(*result, sep='\n')
else:
    print(-1)