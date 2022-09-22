from collections import deque

INF = int(1e9)

T = int(input())
for _ in range(T):
    N = int(input())
    move_type = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    data = []
    for i in range(N):
        data.append(list(map(int, input().split())))

    dist = [[INF] * (N + 1) for _ in range(N + 1)]

    def bfs():
        q = deque()
        q.append((0, 0))
        dist[0][0] = data[0][0]

        while q:
            x, y = q.popleft()
            for move in move_type:
                nx, ny = x + move[0], y + move[1]

                if 0 <= nx < N and 0 <= ny < N:
                    new_dist = dist[x][y] + data[nx][ny]
                    if dist[nx][ny] > new_dist:
                        dist[nx][ny] = new_dist
                        q.append((nx, ny))

    bfs()
    print(dist[N-1][N-1])