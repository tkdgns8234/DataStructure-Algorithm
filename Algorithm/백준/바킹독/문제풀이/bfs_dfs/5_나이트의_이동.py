# 5. 나이트의 이동
from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
# 묶기
for _ in range(T):
    size = int(input())
    data = [[0] * size for i in range(size)]
    now_x, now_y = map(int, input().rstrip().split())
    target_x, target_y = map(int, input().rstrip().split())
    data[now_x][now_y] = 1 # 방문한곳 = 1 이상 거리별 증가
    data[target_x][target_y] = -2 # 타겟 = -2

    if now_x == target_x and now_y == target_y:
        print(0)
        continue

    move_type = [
        (-1, 2),(-2, 1),(-1, -2),(-2, -1),(1, 2),(2, 1),(2, -1),(1, -2)
    ]
    q = deque()
    q.append((now_x,now_y))
    flag = False
    while q:
        x, y = q.popleft()
        for move in move_type:
            nx, ny = x + move[0], y + move[1]
            if nx < 0 or ny < 0 or nx >= size or ny >= size:
                continue
            if data[nx][ny] == 0:
                data[nx][ny] = data[x][y] + 1
                q.append((nx,ny))
            if data[nx][ny] == -2:
                print(data[x][y])
                flag = True
                break
        if flag:
            break
