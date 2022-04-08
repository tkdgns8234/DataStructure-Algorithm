# 9. 구슬 탈출 2
# 그리 어려운 문제는 아니었다 랭크에 쫄지말자
# 시간복잡도:(4*3*3*3 4방향이동 * (n-2)) * 2 * 10 공간복잡도:n**2m**2 방문처리때문
# .는 빈칸 #는 벽 0은 구멍
import sys
from collections import deque
input = sys.stdin.readline

# 한 방향씩 기울여야함
move_type = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def move(direction, x, y):
    count = 0
    while True:
        nx, ny = x + direction[0], y + direction[1]
        if data[nx][ny] == '#':
            return x, y, count, False
        if data[nx][ny] == 'O':
            return 0, 0, 0, True
        x, y = nx, ny
        count += 1

# red, blue 구슬을 한번에 굴린다.
def bfs():
    global min_val, visited
    rx, ry, bx, by = red_pos[0], red_pos[1], blue_pos[0], blue_pos[1]
    q = deque([[rx, ry, bx, by, 0]])  # 0: count
    visited[rx][ry][bx][by] = True

    while q:
        rx, ry, bx, by, count = q.popleft()
        # if count > min_val: # 최적화 <- 필요가 없다, nr_result 값인 red 구슬이 첫번째로 들어갔을 때가 정답이고
        # 바로 return 하면 됨, bfs의 특징
        #     continue
        if count >= 10:
            return
        for mv in move_type:
            nrx, nry, nr_count, nr_result = move(mv, rx, ry)
            nbx, nby, nb_count, nb_result = move(mv, bx, by)

            if nb_result: #blue가 빠진경우 skip
                continue
            if nr_result:
                min_val = min(min_val, count + 1)
                return
            if nrx == nbx and nry == nby: # 좌표가 동일하고
                if nr_count < nb_count: # 더 멀리서 온 경우 한칸 전으로 이동
                    nbx, nby = nbx - mv[0], nby - mv[1]
                else:
                    nrx, nry = nrx - mv[0], nry - mv[1]

            if not visited[nrx][nry][nbx][nby]:
                q.append((nrx,nry,nbx,nby,count + 1))
                visited[nrx][nry][nbx][nby] = True


n, m = map(int, input().split())
data = []
red_pos, blue_pos = (0, 0), (0, 0)
# visited = [[[False] * m for _ in range(n)] * m for _ in range(n)] 틀림, 유의
visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]

for i in range(n):
    line = list(input().rstrip())
    data.append(line)
    for j in range(m):
        if line[j] == 'R':
            red_pos = (i, j)
        elif line[j] == 'B':
            blue_pos = (i, j)
min_val = int(1e9)
bfs()
print(min_val if min_val != int(1e9) else -1)
