# 늑대는 2배의 속도로 간 후 2/1배의 속도로 이동
# 달빛여우가 먼저 도착할 수 있는 그루터기를 찾기

# 최단거리를 2개로 나눠서 생각
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra_fox(start):
    distance = [INF] * (N + 1)
    distance[start] = 0
    q = []

    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


def dijkstra_wolf(start):
    # distance[0] => 빠르게 도착한 경우
    # distance[1] => 느리게 도착한 경우
    distance = [[INF] * (N + 1) for _ in range(2)]
    distance[1][start] = 0
    q = []

    heapq.heappush(q, (0, start, False))
    while q:
        dist, now, is_fast = heapq.heappop(q)
        if is_fast and distance[0][now] < dist:
            continue
        elif not is_fast and distance[1][now] < dist:
            continue

        for i in graph[now]:
            if is_fast:
                # 빠르게 도착한 경우 느리게 간다
                cost = dist + i[1] * 2
                if distance[1][i[0]] > cost:
                    distance[1][i[0]] = cost
                    heapq.heappush(q, (cost, i[0], False))
            else:
                # 느리게 도착한 경우 빠르게 간다
                cost = dist + i[1] / 2
                if distance[0][i[0]] > cost:
                    distance[0][i[0]] = cost
                    heapq.heappush(q, (cost, i[0], True))
    return distance

dist1 = dijkstra_fox(1)
dist2 = dijkstra_wolf(1)

ans = 0
for i in range(1, N+1):
    if dist1[i] < min(dist2[0][i], dist2[1][i]):
        ans += 1

print(ans)
