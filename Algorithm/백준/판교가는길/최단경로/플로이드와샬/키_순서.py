import sys
input = sys.stdin.readline

INF = int(1e9)
N, M = map(int, input().split())
graph = [[INF] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            if graph[a][k] == 1 and graph[k][b] == 1:
                graph[a][b] = 1

ans = 0
for i in range(1, N+1):
    c = 0
    for j in range(1, N+1):
        if graph[i][j] == 1 or graph[j][i] == 1:
            c += 1
    if c == N-1:
        ans += 1
print(ans)