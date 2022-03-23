# 문제4 숨바꼭질
from collections import deque

n, m = map(int, input().split())
visited = [False] * 100001

q = deque()
q.append((n, 0))
visited[n] = True

move_type = [1, -1, 2]
while q:
    now, time = q.popleft()
    if now == m:
        print(time)
        break

    for move in move_type:
        if move == 2:
            n_now = now * 2
        else:
            n_now = now + move
        if 0 <= n_now <= 100000 and not visited[n_now]:
            visited[n_now] = True
            q.append((n_now, time + 1))
