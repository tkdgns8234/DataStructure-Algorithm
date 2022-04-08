# 문제 5. Maaaaaaaaaze
# for 문 말고 btk 형식으로 하려했으나 낭비가 심해보였음
# depp copy 를 해야해서
# 블로그 참조해보자

# import copy
# from collections import deque
# from itertools import permutations
#
# def rotate(arr):
#     x = len(arr)
#     result = [[0] * x for _ in range(x)]
#     for i in range(x):
#         for j in range(x):
#             result[j][x - i - 1] = arr[i][j]
#     return result
#
#
# # 상하좌우 위아래 로 이동 가능
# # 입 & 출구 -> 8개 (4,0,0) (0,4,4) / (040), (404) ....
# move_type = [(0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (-1, 0, 0), (1, 0, 0)]
# in_out = [
#     ([4, 0, 0], [0, 4, 4]),
#     ([0, 4, 0], [4, 0, 4]),
#     ([0, 0, 4], [4, 4, 0]),
#     ([4, 4, 0], [0, 0, 4]),
#     ([4, 0, 4], [0, 4, 0]),
#     ([0, 4, 4], [4, 0, 0]),
#     ([0, 0, 0], [4, 4, 4]),
#     ([4, 4, 4], [0, 0, 0]),
# ]
#
# # 1 -> 참가자가 이동 가능한 칸
# def bfs(io, visited):
#     h, x, y = io[0]
#     out_h, out_x, out_y = io[1]
#     q = deque()
#     q.append((h,x,y,0))
#     visited[h][x][y] = True
#
#     while q:
#         h, x, y, dist = q.popleft()
#         if h == out_h and x == out_x and y == out_y:
#             return dist
#         for move in move_type:
#             nh, nx, ny = h+move[0], x+move[1], y+move[2]
#             if nx < 0 or ny < 0 or nx >= 5 or ny >= 5 or nh < 0 or nh >= 5:
#                 continue
#             if not visited[nh][nx][ny] and temp[nh][nx][ny] == 1:
#                 visited[nh][nx][ny] = True
#                 q.append((nh,nx,ny,dist+1))
#     return int(1e9)
#
#
# #data[높이][x][y]
# data = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
#
# min_val = int(1e9)
#
# permu = list(permutations([0,1,2,3,4],5))
# temp = []
# for per in permu:
#     for p in per:
#         temp.append(data[p])
#         # 4 회 회전하는 모든 경우의수
#     for a in range(4):
#         temp[0] = rotate(temp[0])
#         for b in range(4):
#             temp[1] = rotate(temp[1])
#             for c in range(4):
#                 temp[2] = rotate(temp[2])
#                 for d in range(4):
#                     temp[3] = rotate(temp[3])
#                     for e in range(4):
#                         temp[4] = rotate(temp[4])
#                         for io in in_out:
#                             visited = [[[False] * 5 for _ in range(5)] for _ in range(5)]
#                             min_val = min(min_val, bfs(io, visited))
#
# if min_val == int(1e9):
#     print(-1)
# else:
#     print(min_val)


# 블로그 풀이
from sys import stdin
from itertools import permutations
from collections import deque

input = stdin.readline
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]
INF = 9876543210

board = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
visited_num = 0
answer = INF

def solv():
    for order in permutations(range(5),5):
        stack_board(order,0)
    print(answer if answer != INF else -1)
def stack_board(order,idx):
    global board
    if answer == 12:
        return
    if idx == 5:
        simul(order)
        return
    for _ in range(4):
        board_rotate(order[idx])
        stack_board(order,idx+1)

def simul(order):
    global answer,visited,visited_num
    game_board = []
    for idx in order:
        game_board.append(board[idx])

    visited_num += 1

    start = [0,0,0]
    end = [4,4,4]

    if game_board[start[0]][start[1]][start[2]] != 1 or game_board[end[0]][end[1]][end[2]] != 1:
        return

    visited_num += 1
    q = deque([start+[0]])
    visited[0][start[0]][start[1]] = visited_num
    while q:
        z,x,y,cnt = q.pop()

        if cnt >= answer:
            continue
        if end[0] == z and end[1] == x and end[2] == y:
            answer = min(answer,cnt)
            break

        for d in range(6):

            nz = z + dz[d]
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nz,nx,ny,game_board):
                visited[nz][nx][ny] = visited_num
                q.appendleft((nz,nx,ny,cnt+1))

def point_validator(z,x,y,game_board):
    if z < 0 or x < 0 or y < 0 or z >= 5 or x >= 5 or y >= 5:
        return False
    elif game_board[z][x][y] == 0:
        return False
    elif visited[z][x][y] == visited_num:
        return False
    return True

def board_rotate(z):
    global board

    tmp = []
    for row in board[z]:
        tmp_row = []
        for num in row:
            tmp_row.append(num)
        tmp.append(tmp_row)

    for x in range(5):
        for y in range(5):
            board[z][y][4-x] = tmp[x][y]

solv()


# 문제 5 Maaaaaaaaaze 재풀이
# 문제풀이 방법
# 1. 판의 위치 순열을 permutation을 이용해 설정한다
# 2. 배치된 순서에서 각각 4번씩 회전한다 => 재귀함수 or btk 이용
# 3. 3차원 배열을 bfs로 탐색하여 최단거리를 측정한다
# 최적화 - 변수
# 1. 방문을 여러번 해야하는경우 방문에대한 visit 변수를 bool 자료형이 아닌 숫자로 선언한다
# 2. rotate 시키는것은 temp 변수를통해 copy 하지말고 그냥 돌리자. 360도 모든경우 탐색하면 된다
# 최적화
# 1. 최단거리는 12 이므로 최단거리가 발생한경우 바로 프로그램을 멈춘다
# 2. 입구 or 출구가 막혀있는경우 탐색하지않는다
# 3. 각 입구, 출구는 회전에의해 한 지점씩만 지정하면 된다 (444), (000)
# 성공
# from itertools import permutations
# from collections import deque
# move_type = [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]
# INF = int(1e9)
# def solve():
#     orders = list(permutations(range(5), 5))
#     for order in orders:
#         reculsive(0, order)
#
# def reculsive(depth, order):
#     global min_val
#     if depth == 5:
#         min_val = min(min_val, bfs(order))
#         if min_val == 12: # 최적화 (최단거리 12 인 경우 출력 후 프로그램 종료)
#             print(12)
#             exit()
#         return
#     for k in range(4):
#         rotate(order[depth]) # 여기서 k 값을 넣어서 틀렸었다 아직 재귀에 익숙하지가 않아 왜 k 는 안되는지 이유를 살펴보자 -> 설계관점에서
#         #4번 회전시키려고 쓴거야,,
#         # k 로 하면 계속 0번째부터 회전함.. 내가 원하는게 아니었음
#         reculsive(depth+1, order)
#
#
# def bfs(order):
#     global visit_num
#
#     start = [0,0,0]
#     end = [4,4,4]
#
#     # order에따라 배열 새로 생성
#     temp = []
#     for o in order:
#         temp.append(data[o])
#
#     if temp[start[0]][start[1]][start[2]] == 0 or temp[end[0]][end[0]][end[0]] == 0:
#         return INF # 입구 출구가 막혀있는 경우
#
#     visit_num += 1
#     q = deque([start + [0]])
#     visited[start[0]][start[1]][start[2]] = visit_num
#
#     while q:
#         h, x, y, dist = q.popleft()
#         if h == end[0] and x == end[1] and y == end[2]:
#             return dist
#         for move in move_type:
#             nh, nx, ny = h + move[0], x + move[1], y + move[2]
#             if point_validator(nh, nx, ny, temp):
#                 visited[nh][nx][ny] = visit_num
#                 q.append((nh, nx, ny, dist + 1))
#     return INF
#
#
# def point_validator(nh, nx, ny, temp):
#     if nh < 0 or nx < 0 or ny < 0 or nh >= 5 or nx >= 5 or ny >= 5:
#         return False
#     if temp[nh][nx][ny] == 0:
#         return False
#     if visited[nh][nx][ny] == visit_num:
#         return False
#     return True
#
#
# def rotate(k):
#     result = [[0]*5 for _ in range(5)]
#     length = 5
#     for i in range(5):
#         for j in range(5):
#             result[j][length-i-1] = data[k][i][j]
#     data[k] = result
#     return
#
# data = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
# visited = [[[0]*5 for _ in range(5)] for _ in range(5)]
# visit_num = 0
# min_val = INF
# solve()
# if min_val == INF:
#     print(-1)
# else:
#     print(min_val)