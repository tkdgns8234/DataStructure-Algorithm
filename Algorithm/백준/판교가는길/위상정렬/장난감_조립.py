# 선후관계가 명확하고 싸이클이 존재하지 않으므로 (두 중간 부품이 서로를 필요로 하는 경우가 없다)
# 위상 정렬을 사용한다는것은 쉽게 알 수 있다.
# 근데 어려웠던 점이 있었다. 간선상의 비용이 존재하는 형태라는것
# 이 비용을 어떻게 처리할지 몰라서 많이 해맸다.
# 2차원배열의 비용테이블을 만든다.
# 제품x축을 만드는데 필요한 y축의 갯수
# 기본 부품인 경우와 중간부품인 경우를 다르게 처리해야한다

from collections import deque
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
in_degree = [0] * (N+1)
cost = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[b].append((a, c))
    in_degree[a] += 1

q = deque()

for i in range(1, N+1):
    if in_degree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    for next, c in graph[now]:
        # 기본 부품인 경우
        if cost[now].count(0) == N+1:
            cost[next][now] += c
        # 중간 부품인 경우
        else:
            for i in range(1, N+1):
                cost[next][i] += cost[now][i] * c
        in_degree[next] -= 1
        if in_degree[next] == 0:
            q.append(next)

for i in enumerate(cost[N]):
    if i[1] != 0:
        print(*i)