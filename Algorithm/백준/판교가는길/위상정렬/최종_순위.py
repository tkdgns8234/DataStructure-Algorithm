# 우선순위에따라 나열해야하는 문제
# 작년 우선순위가 주어지고, 우선순위가 바뀐 팀이 존재
# 일반적인 위상정렬로 간선 처리 시, 5->4->3->2->1 일 때
# 2 와 4의 순위가 바뀐다고 가정 할 때
# 2와 4의 순위가 바뀐다고 해서, 3과 4와의 관계가 바뀌진 않는다.
# 따라서 모든 정점간의 간선을 표시해야 한다.

# 우선 기존 순위대로 모든 정점간의 간선을 표시하고,
# 순위가 바뀐경우
# graph 와 indegree 를 변경

# 1. 확실한 순위를 만들 수 없는 경우가 있다. -> q에 원소가 2개이상인게 있다.
# 2. 일관성이 없다 -> 싸이클이 발생했다, q가 N번 돌기 전에 끝난다. 라는 얘기
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    indegree = [0] * (N+1)

    # 기존 순위대로 모든 정점간의 간선 표시
    # 순위가 높은곳의 진입차수가 0에 가까워야 위상 정렬 수행 시, 원하는 대로 순위를 뽑아낼 수 있음
    # -> 순위가 높은곳에서 낮은곳으로 간선 표시
    graph = [[] for _ in range(N+1)]
    for i in range(N):
        for j in range(i+1, N):
            graph[data[i]].append(data[j])
            indegree[data[j]] += 1

    M = int(input())
    # 순위 변경
    for _ in range(M):
        a, b = map(int, input().split())
        flag = True

        for i in graph[a]:
            if i == b: # a가 우선순위 더 높은경우 반대로 변경
                graph[a].remove(b)
                indegree[a] += 1
                graph[b].append(a)
                indegree[b] -= 1
                flag = False
        if flag: # a가 우선순위 더 낮은경우
            graph[b].remove(a)
            indegree[b] += 1
            graph[a].append(b)
            indegree[a] -= 1

    certain = True
    count = 0
    result = []

    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        if len(q) > 1:
            certain = False
            break
        count += 1

        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    if not certain:
        print("?")
    elif count < N: # 싸이클 발생
        print("IMPOSSIBLE")
    else:
        print(*result, sep=" ")