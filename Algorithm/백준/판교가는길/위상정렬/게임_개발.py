import sys
from collections import deque
input = sys.stdin.readline

INF = int(1e9)
N = int(input())

indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
time = [INF] * (N+1)

for i in range(1, N+1):
    info = list(map(int, input().split()))[:-1]
    time[i] = info[0]
    for j in info[1:]:
        graph[j].append(i)
        indegree[i] += 1

result = [0] * (N+1)
def topology_sort():
    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        # 선수건물의 최댓값 + 현재 건물의 값
        result[now] += time[now]

        for i in graph[now]:
            indegree[i] -= 1
            # 선수 건물의 최댓값으로 설정
            result[i] = max(result[i], result[now])
            if indegree[i] == 0:
                q.append(i)

topology_sort()
for i in range(1, N+1):
    print(result[i])