# 이분탐색 + 그래프
import heapq
import sys

input = sys.stdin.readline

def solve(weight):
    visited = [False]*(N+1)
    # 최대 무게를 위해 최대 힙으로 구현
    q = [-S]
    visited[S] = True
    while q:
        now = -(heapq.heappop(q))

        if now == T:
            return True

        for node, w in graph[now]:
            if not visited[node] and w >= weight:
                visited[node] = True
                heapq.heappush(q, -node)
    return False

def binary_search(start, end):
    global ans
    while start <= end:
        mid = (start+end)//2
        if solve(mid):
            ans = max(ans, mid)
            start = mid + 1
        else:
            end = mid - 1

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
max_weight = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    max_weight = max(max_weight, c)

S, T = map(int, input().split())

ans = 0
binary_search(0, max_weight)
print(ans)