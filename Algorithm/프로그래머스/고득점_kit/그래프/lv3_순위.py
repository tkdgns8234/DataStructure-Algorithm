# 순위관련 문제는 두 번 풀었던 기억이 있다.
# 한번은 위상정렬, 한번은 플로이드 로 풀었던거같은데
# 순위를 알려면 특정 노드에서 다른 노드까지 향하는 길이 존재하는지 확인해야한다
# 모든 노드에서 모든 노드까지의 간선이 존재하는지 확인
# -> 플로이드 -> 와샬 알고리즘이 떠오른다
# INF 는 도달할 수 없다는 뜻
# 구현해보자

# 틀린거같다 우선순위와 상관없이 도착 가능 여부를 판단할수있는거같은데
# -> 아니네 잘 해결 했네,
# 우선
# 아래 반복문에서 graph[b][a] = 1 도 추가했는데
# 이러면 우선순위 상관없이 노드를 넘나들 수 있기때문에 추가하면 안된다.
# for a, b in results:
#     graph[a][b] = 1
# 이후 마지막 반복문에서 a->b 또는 b->a로 연결되어있는지 모든 노드를 확인하면 된다.

# INF = int(1e9)
# def solution(n, results):
#     graph = [[INF] * (n+1) for _ in range(n+1)]
#
#     for i in range(1, n+1):
#         graph[i][i] = 0
#
#     for a, b in results:
#         graph[a][b] = 1
#
#     for k in range(1, n+1):
#         for i in range(1, n+1):
#             for j in range(1, n+1):
#                 if i == j:
#                     continue
#                 graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
#
#
#     answer = 0
#     for i in range(1, n+1):
#         flag = True
#         for j in range(1, n+1):
#             if graph[i][j] == INF and graph[j][i] == INF:
#                 flag = False
#                 break
#         if flag:
#             answer += 1
#     return answer
#
# v = solution(5,	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])
# print(v)

# 다른 사람의 좋은 코드
# set + dict 자료구조 활용
from collections import defaultdict
def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    for result in results:
            lose[result[1]].add(result[0])
            win[result[0]].add(result[1])

    for i in range(1, n + 1):
        for winner in lose[i]: win[winner].update(win[i])
        for loser in win[i]: lose[loser].update(lose[i])

    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n - 1: answer += 1
    return answer

solution(5,	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])