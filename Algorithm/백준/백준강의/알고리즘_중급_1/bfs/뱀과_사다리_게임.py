from collections import deque

visited = [False]*101

N, M = map(int, input().split())
ladders = dict()
snakes = dict()
for i in range(N):
    start, end = map(int, input().split())
    ladders[start] = end
for i in range(M):
    start, end = map(int, input().split())
    snakes[start] = end

q = deque([(1,0)])
while q:
    now, dist = q.popleft()

    if now == 100:
        print(dist)
        exit(0)

    for i in range(1, 7):
        next = now + i
        if next == 12:
            pass
        if next > 100: break
        if not visited[next]:
            if next in snakes:
                next = snakes[next]
            elif next in ladders:
                next = ladders[next]

            q.append((next, dist + 1))
            visited[next] = True