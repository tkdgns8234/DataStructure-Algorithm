# 문제 1. puyo puyo
# down()함수인 바닥으로 내리는거 실패 ㅋㅋ; 좌절감 쎄게 오네 별것도 아닌거같은데 거기서 막혀서
# 블로그 참조
from collections import deque
move_type = [(-1, 0),(1, 0),(0, 1),(0, -1)]

def down():
    # q를 이용하는 방법
    # 참고: https://in0-pro.tistory.com/19
    # 훨~~~~씬 쉽다
    for j in range(6):
        q = deque()
        for i in range(11, -1, -1):
            if data[i][j] != '.':
                q.append(data[i][j])
        for i in range(11, -1, -1):
            if q:
                data[i][j] = q.popleft()
            else:
                data[i][j] = '.'

    # for문으로 돌리는 방법 너무 어려움..
    # for j in range(6):
    #     for i in range(10, -1, -1):
    #         if data[i][j] != '.' and data[i+1][j] == '.':
    #             for k in range(i + 1, 12):
    #                 if k == 11 and data[k][j] == '.':
    #                     data[k][j] = data[i][j]
    #                 elif data[k][j] != '.':
    #                     data[k-1][j] = data[i][j]
    #                     break
    #             data[i][j] = '.'

def bomb(x, y): # 터진상태는 . 로 전환
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    pivot = data[x][y]
    count = 1
    l = [(x,y)]
    while q:
        x, y = q.popleft()
        for move in move_type:
            nx, ny = move[0] + x, move[1] + y
            if (nx < 0 or ny < 0 or nx >= 12 or ny >= 6) or visited[nx][ny]:
                continue
            if data[nx][ny] == pivot:
                q.append((nx,ny))
                visited[nx][ny] = True
                count += 1
                l.append((nx, ny))

    if count >= 4:
        for lx, ly in l:
            data[lx][ly] = '.'
        return True
    return False


data = [list(input()) for _ in range(12)]
count = 0
bombed = True
while bombed:
    visited = [[False] * 6 for i in range(12)]
    bombed = False
    for i in range(12):
        for j in range(6):
            if data[i][j] != '.':
                if bomb(i, j):
                    bombed = True
    if bombed:
        count += 1
        down()

print(count)