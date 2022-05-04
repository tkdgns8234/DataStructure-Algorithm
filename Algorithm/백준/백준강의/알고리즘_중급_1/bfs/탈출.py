# 물부터 채우고
# 고슴도치 이동
# 최단거리 출력

from collections import deque

def move_water():
    global water
    temp = set()
    for x,y in water:
        temp.add((x,y))
        for move in move_type:
            nx, ny = x+move[0],y+move[1]
            if 0<=nx<N and 0<=ny<M and board[nx][ny] != 'X' and board[nx][ny] != 'D':
                temp.add((nx,ny))
    water = temp

def bfs(start):
    q = deque([start])
    visited[start[0]][start[1]] = True
    cnt = 0
    while q:
        move_water()
        len_q = len(q)
        for _ in range(len_q):
            x, y = q.popleft()
            if board[x][y] == 'D':
                return cnt
            for move in move_type:
                nx, ny = x+move[0],y+move[1]
                if 0<=nx<N and 0<=ny<M and board[nx][ny] != '*' and board[nx][ny] != 'X':
                    if not visited[nx][ny] and (nx, ny) not in water:
                        visited[nx][ny] = True
                        q.append((nx, ny))
        cnt += 1
    return 'KAKTUS'



move_type = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, M = map(int, input().split())
visited = [[False]*M for _ in range(N)]
board = []
water = set()
for i in range(N):
    row = list(input())
    for j in range(M):
        if row[j] == 'S':
            start = (i, j)
        elif row[j] == '*':
            water.add((i,j))
    board.append(row)

print(bfs(start))
