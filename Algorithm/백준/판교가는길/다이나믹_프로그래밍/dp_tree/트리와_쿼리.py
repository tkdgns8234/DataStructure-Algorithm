import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e7))

V, R, Q = map(int, input().split())
graph = [[] for _ in range(V+1)]
for i in range(V-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [0] * (V+1)
visited = [False] * (V+1)

def solve(n):
    visited[n] = True
    dp[n] = 1

    for i in graph[n]:
        if not visited[i]:
            solve(i)
            dp[n] += dp[i]

solve(R)

for _ in range(Q):
    n = int(input())
    print(dp[n])