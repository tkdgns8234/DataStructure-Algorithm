# 성공했는데 넘 복잡..
import collections

move_type = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def point_validator(n1, n2):
    n1_x, n1_y, n2_x, n2_y = n1[0], n1[1], n2[0], n2[1]
    if 0 <= n1_x < N and 0 <= n1_y < N:
        if 0 <= n2_x < N and 0 <= n2_y < N:
            if visited[n1_x][n1_y][n2_x][n2_y] == False and\
                    Board[n1_x][n1_y]== 0 and Board[n2_x][n2_y] == 0:
                return True
    return False

def rotate(now):
    available = []
    n1_x, n1_y, n2_x, n2_y = now[0][0], now[0][1], now[1][0], now[1][1]
    # 가로 상태
    if n1_x == n2_x:
        for i in (1, -1): #1: 아래 -1: 위
            if 0 <= n1_x+i < N and 0 <= n1_y < N:
                if 0 <= n2_x+i < N and 0 <= n2_y < N:
                    if Board[n1_x + i][n1_y] == 0 and Board[n2_x + i][n2_y] == 0:
                        available.append(([n1_x, n1_y], [n1_x+i, n1_y]))
                        available.append(([n2_x, n2_y], [n2_x+i, n2_y]))
    # 세로 상태
    elif n1_y == n2_y:
        for i in (1, -1): #-1 왼쪽 1 오른쪽
            if 0 <= n1_x < N and 0 <= n1_y+i < N:
                if 0 <= n2_x < N and 0 <= n2_y+i < N:
                    if Board[n1_x][n1_y + i] == 0 and Board[n2_x][n2_y + i] == 0:
                        available.append(([n1_x, n1_y], [n1_x, n1_y+i]))
                        available.append(([n2_x, n2_y], [n2_x, n2_y+i]))

    return available

Board, visited = [], []
N = 0
def solution(board):
    global N, visited, Board
    Board = board
    N = len(board)

    visited = [[[[False] * N for _ in range(N)] for _ in range(N)] for _ in range(N)]
    start = ([0,0], [0,1], 0) # 0 -> dist
    q = collections.deque([start])
    while q:
        now = q.popleft()
        if now[0][0] == 0 and now[0][1] == 2 and now[1][0] == 1 and now[1][1] == 2:
            pass
        if (now[0][0] == N-1 and now[0][1] == N-1) or (now[1][0] == N-1 and now[1][1] == N-1):
            return now[2]

        for move in move_type:
            n1 = [now[0][0] + move[0], now[0][1] + move[1]]
            n2 = [now[1][0] + move[0], now[1][1] + move[1]]
            if point_validator(n1, n2):
                visited[n1[0]][n1[1]][n2[0]][n2[1]] = True
                dist = now[2] + 1
                q.append((n1, n2, dist))
        # 회전
        for n1, n2 in rotate(now):
            if point_validator(n1, n2):
                visited[n1[0]][n1[1]][n2[0]][n2[1]] = True
                dist = now[2] + 1
                q.append((n1, n2, dist))

v = solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])
print(v)




# 아래는 이코테 코드

from collections import deque

def get_next_pos(pos, board):
    next_pos = []  # 이동가능한 위치들
    pos = list(pos)  # 집합 -> 리스트
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    # [상, 하, 좌, 우]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 모든 방향 확인
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + \
                                                             dy[i]
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
    # 로봇이 가로로 놓여있는 경우
    if pos1_x == pos2_x:
        for i in [-1, 1]:  # 위쪽으로 회전하거나, 아래쪽으로 회전
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:  # 위쪽 혹은 아래쪽 두 칸이 모두 비어있다면
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    # 로봇이 세로로 놓여있는 경우
    elif pos1_y == pos2_y:
        for i in [-1, 1]:  # 위쪽으로 회전하거나, 아래쪽으로 회전
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:  # 위쪽 혹은 아래쪽 두 칸이 모두 비어있다면
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
    # 현재 위치에서 이동할 수 있는 위치 반환
    return next_pos


def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}
    q.append((pos, 0))
    visited.append(pos)  # 방문처리

    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            return cost
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0