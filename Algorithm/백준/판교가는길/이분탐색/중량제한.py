# 최적화만 잘 하면 그냥 dfs만으로도 풀 수 있지 않을까? 라고 생각했던게 틀렸다
# 시간복잡도가 재대로 계산되진 않지만 가능할거같았는데,, 역시 넘겨짚으면 안되는군
# BFS + 이진탐색문제이다
# 이진탐색으로 무게를 구한 후
# bfs로 해당 위치에 도착할 수 있는지 확인한다.

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(int(1e5)+1)
#
# N, M = map(int, input().split())
# graph = [[] for _ in range(N+1)]
# maximum_weight = [0] * (N+1)
#
# for i in range(M):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))
#     graph[b].append((a, c))
#
# start, end = map(int, input().split())
#
# def dfs(num, w):
#     print(num)
#     global ans
#     if maximum_weight[num] < w:
#         maximum_weight[num] = w
#     else:
#         return
#     if num == end:
#         ans = max(ans, w)
#         return
#
#     for b, c in graph[num]:
#         dfs(b, min(w, c))
#
# ans = 0
# dfs(start, int(1e10))
# print(ans)


import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
max_c = 0

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    max_c = max(max_c, c)

start_island, end_island = map(int, input().split())

def bfs(weight):
    visited = [False] * (N+1)
    visited[start_island] = True
    q = deque([start_island])

    while q:
        now = q.popleft()

        if now == end_island:
            return True

        for b, c in graph[now]:
            if not visited[b] and c >= weight:
                visited[b] = True
                q.append(b)
    return False


def search():
    global ans
    s, e = 1, max_c
    while s <= e:
        mid = (s+e)//2
        if bfs(mid):
            ans = mid
            s = mid + 1
        else:
            e = mid - 1


ans = 0
search()
print(ans)


