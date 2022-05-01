from collections import deque

N = int(input())
temp = list(map(int, input().split()))
start = temp[0:2]
target = temp[2:4]
visited = [[False]*N for _ in range(N)]

q = deque([start+[0]])
while q:
    x, y, dist = q.popleft()
    if x == target[0] and y == target[1]:
        print(dist)
        exit(0)

    move_type = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
    for move in move_type:
        nx = x + move[0]
        ny = y + move[1]
        if 0<=nx<N and 0<=ny<N:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append([nx, ny, dist+1])
print(-1)