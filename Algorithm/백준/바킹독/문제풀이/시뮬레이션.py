# 문제 1. puyo puyo
# down()함수인 바닥으로 내리는거 실패 ㅋㅋ; 좌절감 쎄게 오네 별것도 아닌거같은데 거기서 막혀서
# 블로그 참조
# from collections import deque
# move_type = [(-1, 0),(1, 0),(0, 1),(0, -1)]
#
# def down():
#     # q를 이용하는 방법
#     # 참고: https://in0-pro.tistory.com/19
#     # 훨~~~~씬 쉽다
#     for j in range(6):
#         q = deque()
#         for i in range(11, -1, -1):
#             if data[i][j] != '.':
#                 q.append(data[i][j])
#         for i in range(11, -1, -1):
#             if q:
#                 data[i][j] = q.popleft()
#             else:
#                 data[i][j] = '.'
#
#     # for문으로 돌리는 방법 너무 어려움..
#     # for j in range(6):
#     #     for i in range(10, -1, -1):
#     #         if data[i][j] != '.' and data[i+1][j] == '.':
#     #             for k in range(i + 1, 12):
#     #                 if k == 11 and data[k][j] == '.':
#     #                     data[k][j] = data[i][j]
#     #                 elif data[k][j] != '.':
#     #                     data[k-1][j] = data[i][j]
#     #                     break
#     #             data[i][j] = '.'
#
# def bomb(x, y): # 터진상태는 . 로 전환
#     q = deque()
#     q.append((x, y))
#     visited[x][y] = True
#     pivot = data[x][y]
#     if pivot == 'R':
#         pass
#     count = 1
#     l = [(x,y)]
#     while q:
#         x, y = q.popleft()
#         for move in move_type:
#             nx, ny = move[0] + x, move[1] + y
#             if (nx < 0 or ny < 0 or nx >= 12 or ny >= 6) or visited[nx][ny]:
#                 continue
#             if data[nx][ny] == pivot:
#                 q.append((nx,ny))
#                 visited[nx][ny] = True
#                 count += 1
#                 l.append((nx, ny))
#
#     if count >= 4:
#         for lx, ly in l:
#             data[lx][ly] = '.'
#         return True
#     return False
#
#
# data = [list(input()) for _ in range(12)]
# count = 0
# bombed = True
# while bombed:
#     visited = [[False] * 6 for i in range(12)]
#     bombed = False
#     for i in range(12):
#         for j in range(6):
#             if data[i][j] != '.':
#                 if bomb(i, j):
#                     bombed = True
#     if bombed:
#         count += 1
#         down()
#
# print(count)

# 문제2. 톱니바퀴
# 잘 풀었는데 개선할점이 많다
# 1. deque를 여러개 만들 수 있다
# list 안에 deque들을 담는 형식으로
# 2. 톱니를 돌리는 dfs 함수를 개선할 수 있다
# 좌 확인, 우 확인 하는 함수를 만들면 돼
# 거기서 재귀호출
# 3. deque에서 rotate 라는 함수로 실제회전시킬 수 있다
# https://hapbbying.tistory.com/64
# 개선의 여지가 많다 다시 풀어보자.

# import sys
# input = sys.stdin.readline
#
# # deque 로 구현하려니까 배열형태로 쓸 수 없으니 너무 복잡해진다
# # list로 구현하자
#
# def dfs(t_num, side):
#     if visited[t_num]:
#         return
#     visited[t_num] = True
#
#     l = [] # 호출해야할 톱니
#     if t_num == 1 or t_num == 2:
#         # 좌 우 확인
#         # 좌
#         if T[t_num-1][2] != T[t_num][6]:
#             l.append(t_num-1)
#         # 우
#         if T[t_num+1][6] != T[t_num][2]:
#             l.append(t_num+1)
#
#     elif t_num == 0:
#         # 우만 확인
#         if T[t_num + 1][6] != T[t_num][2]:
#             l.append(t_num + 1)
#     elif t_num == 3:
#         # 좌만 확인
#         if T[t_num-1][2] != T[t_num][6]:
#             l.append(t_num-1)
#     # 회전 후 호출
#     # 회전
#     if side == 1: #시계
#         v = T[t_num].pop()
#         T[t_num].insert(0, v)
#     else: #반시계
#         v = T[t_num].pop(0)
#         T[t_num].append(v)
#     for num in l:
#         dfs(num, -side)
#
# # 0: N 1: S
# T = [list(input().rstrip()) for _ in range(4)]
# K = int(input()) # 회전 횟수
# op = [list(map(int, input().rstrip().split())) for _ in range(K)]
#
# # side 1: 시계방향 -1: 반시계방향
# for t_num, side in op:
#     visited = [False] * 4
#     dfs(t_num-1, side)
#
# score = 0
# for i in range(4):
#     if T[i][0] == '1':
#         score += 2 ** i
# print(score)

# 문제 3. 주사위 굴리기
# 풀어봤던 문제야,, 틀리지말자
# 주사위를 어떻게 처리할지 또 떠오르지 않았어,, 블로그 살짝 참고 다시풀이
# 주사위를 1차원배열로 표현

# import sys
# input = sys.stdin.readline
# n, m, x, y, k = map(int, input().rstrip().split())
# data = [list(map(int, input().rstrip().split())) for i in range(n)]
# sides = list(map(int, input().rstrip().split()))
# # 1차원 배열로 주사위 표현
# # 위, 북, 동, 서, 남, 아래
# dice = [None] + [0 for i in range(6)]
#
# move_type = [None, (0, 1), (0,-1), (-1, 0), (1,0)]
#
# for side in sides:
#     nx, ny = x+move_type[side][0], y+move_type[side][1]
#     if nx < 0 or ny < 0 or nx >= n or ny >= m:
#         continue
#     if side == 1: # 동
#         dice[3],dice[1],dice[4],dice[6] = dice[1],dice[4],dice[6],dice[3]
#     if side == 2:  # 서
#         dice[4],dice[6],dice[3],dice[1] = dice[1],dice[4],dice[6],dice[3]
#     if side == 3:  # 북
#         dice[1],dice[2],dice[6],dice[5] = dice[5],dice[1],dice[2],dice[6]
#     if side == 4:  # 남
#         dice[2],dice[1],dice[5],dice[6] = dice[6],dice[2],dice[1],dice[5]
#
#     # 이동한 칸에 쓰인 수가 0이면
#     if data[nx][ny] == 0:
#         data[nx][ny] = dice[6]
#     else:
#         dice[6] = data[nx][ny]
#         data[nx][ny] = 0
#     print(dice[1])
#     x, y = nx, ny

# 문제 4. 트럭
# 최대 10만의 시간 소요: 시간복잡도 충분
# 지문 자체를 이해하는데 오래걸렸어;;
# from collections import deque
# # 트럭수, 다리길이, 다리 최대 하중
# n, bride_l, birdge_w = map(int, input().split())
# truck = list(map(int, input().split()))
#
# second = 0 # 소요 시간
# truck_w = 0 # 총 트럭 무게
# index = 1 # 몇 번째 트럭이 들어갈 차례인지
#
# q = deque()
# q.append((truck[0], 0 + bride_l))  # (무게, 종료시간)
# truck_w += truck[0]
# while q:
#     second += 1
#
#     if q[0][1] == second:
#         temp = q.popleft()
#         truck_w -= temp[0]
#
#     if index < n and (birdge_w - (truck_w + truck[index])) >= 0:
#         q.append((truck[index], second + bride_l))
#         truck_w += truck[index]
#         index += 1
#
# print(second + 1)

# 문제4. 트럭
# 보기에 좀 더 간단해보이고 좋은코드를 찾았다
# bridge 를 실제로 만들고 트럭을 붙이는 형식

# import sys
# from _collections import deque
# input = sys.stdin.readline
#
# N, W, L = map(int, input().split())
# trucks = deque(list(map(int, input().split())))
#
# answer = 0
# bridge = deque([0 for _ in range(W)])
#
# while trucks:
#     bridge.popleft()
#     if sum(bridge) + trucks[0] <= L:
#         truck = trucks.popleft()
#         bridge.append(truck)
#     else:
#         bridge.append(0)
#     answer += 1
# answer += W
# print(answer)

# 문제 5. Maaaaaaaaaze
# for 문 말고 btk 형식으로 하려했으나 낭비가 심해보였음
# depp copy 를 해야해서
# 블로그 참조해보자

import copy
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
# from sys import stdin
# from itertools import permutations
# from collections import deque
#
# input = stdin.readline
# dx = [-1,1,0,0,0,0]
# dy = [0,0,-1,1,0,0]
# dz = [0,0,0,0,-1,1]
# INF = 9876543210
#
# board = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
# visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
# visited_num = 0
# answer = INF
#
# def solv():
#     for order in permutations(range(5),5):
#         stack_board(order,0)
#     print(answer if answer != INF else -1)
# def stack_board(order,idx):
#     global board
#     if answer == 12:
#         return
#     if idx == 5:
#         simul(order)
#         return
#     for _ in range(4):
#         board_rotate(order[idx])
#         stack_board(order,idx+1)
#
# def simul(order):
#     global answer,visited,visited_num
#     game_board = []
#     for idx in order:
#         game_board.append(board[idx])
#
#     visited_num += 1
#
#     start = [0,0,0]
#     end = [4,4,4]
#
#     if game_board[start[0]][start[1]][start[2]] != 1 or game_board[end[0]][end[1]][end[2]] != 1:
#         return
#
#     visited_num += 1
#     q = deque([start+[0]])
#     visited[0][start[0]][start[1]] = visited_num
#     while q:
#         z,x,y,cnt = q.pop()
#
#         if cnt >= answer:
#             continue
#         if end[0] == z and end[1] == x and end[2] == y:
#             answer = min(answer,cnt)
#             break
#
#         for d in range(6):
#
#             nz = z + dz[d]
#             nx = x + dx[d]
#             ny = y + dy[d]
#
#             if point_validator(nz,nx,ny,game_board):
#                 visited[nz][nx][ny] = visited_num
#                 q.appendleft((nz,nx,ny,cnt+1))
#
# def point_validator(z,x,y,game_board):
#     if z < 0 or x < 0 or y < 0 or z >= 5 or x >= 5 or y >= 5:
#         return False
#     elif game_board[z][x][y] == 0:
#         return False
#     elif visited[z][x][y] == visited_num:
#         return False
#     return True
#
# def board_rotate(z):
#     global board
#
#     tmp = []
#     for row in board[z]:
#         tmp_row = []
#         for num in row:
#             tmp_row.append(num)
#         tmp.append(tmp_row)
#
#     for x in range(5):
#         for y in range(5):
#             board[z][y][4-x] = tmp[x][y]
#
# solv()


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
#         rotate(order[depth]) # 여기서 k 값을 넣어서 틀렸었다 아직 재귀에 익숙하지가 않아 왜 k 는 안되는지 이유를 살펴보자
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

# 6.로봇청소기
# 성공! 너무 잘했다 ㅎ
# # 북 동 남 서
# move_type = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#
# # 현재 방향에서 왼쪽방향 반환
# def re_direction(direction):
#     # 북 동 남 서
#     if direction == 0:
#         return 3
#     elif direction == 1:
#         return 0
#     elif direction == 2:
#         return 1
#     elif direction == 3:
#         return 2
#
#
# def clean(x, y, d, depth):
#     global count
#     # c
#     if depth == 4:
#         # 후진
#         back_x, back_y = x-move_type[d][0], y-move_type[d][1]
#         if data[back_x][back_y] == 1:
#             print(count + 1)
#             exit()
#         clean(back_x, back_y, d, 0)
#
#     # 1. 현재위치 청소
#     visited[x][y] = 1
#     # 2. 현재위치에서 현재 방향기준 왼쪽방향 탐색
#     rd = re_direction(d)
#     nx = x + move_type[rd][0]
#     ny = y + move_type[rd][1]
#
#     # a
#     if point_validation(nx, ny):
#         visited[nx][ny] = 1
#         count += 1
#         clean(nx, ny, rd, 0)
#     # b
#     else:
#         clean(x, y, rd, depth + 1)
#
# def point_validation(x, y):
#     if x < 0 or y < 0 or x >= n or y >= m:
#         return False
#     if visited[x][y] == 1:
#         return False
#     if data[x][y] == 1:
#         return False
#     return True
#
# n, m = map(int, input().split())
# x, y, d = map(int, input().split())
# # 빈칸:0 벽:1
# data = [list(map(int, input().split())) for _ in range(n)]
# visited = [[0] * m for i in range(n)]
# count = 0
# clean(x, y, d, 0)
# print(count + 1)

# 7. 테트로미노
# ㅗ 모양 제외하고 나머지 모든 모양은 dfs로 4 칸 이동했을때의 모양이다
# 각 모든지점에서 dfs를 4번 수행하고 최댓값을 구한 후
# ㅗ 모양에대해서는 따로 처리한다 => rotate 함수 필요해보임
# 배치를 어떻게해야할지 감이안오는데?
# 해당 문제를 2가지 방식으로 풀자
# 1. ㅗ 스티커를 직접 붙이는걸 하나 추가한 방식
# 2. dfs에서 모든걸 해결하는 방식

# 1. ㅗ 스티커 하나 붙이는 방식
# dfs 4개 수행 후 (당연히 모든 시작점에서 해야겠지)
# 스티커를 붙이는 경우와 dfs 돌리는경우 두가지 모두 학습했다 성공
# 2번방식으로 다시풀자
# n, m = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(n)]
# visited = [[0] * m for _ in range(n)]
# ans = 0
#
# move_type = [(-1, 0), (1, 0), (0, 1), (0, -1)]
# def dfs(x, y, depth, total):
#     global ans
#     if depth == 3:
#         ans = max(ans, total)
#         return
#
#     for move in move_type:
#         nx, ny = x + move[0], y + move[1]
#         if nx < 0 or ny < 0 or nx >= n or ny >= m:
#             continue
#         if visited[nx][ny] == 0:
#             visited[nx][ny] = 1
#             dfs(nx, ny, depth + 1, total + data[nx][ny])
#             visited[nx][ny] = 0
#
#
# for i in range(n):
#     for j in range(m):
#         visited[i][j] = 1
#         dfs(i, j, 0, data[i][j])
#         visited[i][j] = 0
#
# # ㅗ 에대한 처리
# # 스티커 붙이기 형식
# def attatch(x, y, arr):
#     total = 0
#     for i in range(len(arr)):
#         for j in range(len(arr[0])):
#             if arr[i][j] == 1:
#                 total += data[x+i][y+j]
#     return total
#
# def rotation(arr):
#     temp = [[0] * len(arr) for _ in range(len(arr[0]))]
#     for i in range(len(arr)):
#         for j in range(len(arr[0])):
#             temp[j][len(arr)-i-1] = arr[i][j]
#     return temp
#
# sticker = [[0, 1, 0], [1, 1, 1]]
# count = 0
# while count < 4:
#     count += 1
#     sticker = rotation(sticker)
#     for i in range(n-len(sticker)+1):
#         for j in range(m-len(sticker[0])+1):
#             ans = max(ans, attatch(i, j, sticker))
#
# print(ans)

# 테트로미노 2. dfs에서 모든걸 해결하는 방식
# 최적화까지 생각하자 오래걸리는듯 싶다
# 시간복잡도: O nm * 4 *3 *3  // 4 *4 *4 가 아닌이유는 전단계는 방문했기때문, 4**4가 아닌 이유는 첫번째의경우 방문 하고 시작하기때문
# 공간복잡도: Onm
# dfs 백트래킹 돌릴 때 최적화 (가지치기가 정말 중요하다)

# n, m = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(n)]
# visited = [[False] * m for i in range(n)]
# ans = 0
#
# move_type = [(-1, 0), (1, 0), (0, 1), (0, -1)]
# def dfs(depth, x, y, total):
#     global ans
#     # 가지치기 하면 시간이 극적으로 줄어들어! 1000ms -> 200ms 까지 줄어듬
#     if ans >= total + (max_val * (3-depth)):
#         return
#     if depth == 3:
#         ans = max(ans, total)
#         return
#     for move in move_type:
#         nx, ny = x + move[0], y + move[1]
#         if nx < 0 or ny < 0 or nx >= n or ny >= m :
#             continue
#         if not visited[nx][ny]:
#             if depth == 1:
#                 # 다음 위치를 간것처럼 처리 후 현재 좌표 그대로 이동
#                 visited[nx][ny] = True
#                 dfs(depth + 1, x, y, data[nx][ny] + total)
#                 visited[nx][ny] = False
#             visited[nx][ny] = True
#             dfs(depth + 1, nx, ny, data[nx][ny]+total)
#             visited[nx][ny] = False
#
# max_val = max(map(max, data))
# for i in range(n):
#     for j in range(m):
#         visited[i][j] = True
#         dfs(0, i, j, data[i][j])
#         visited[i][j] = False
#
# print(ans)


# 8. 구슬 탈출 2
# 그리 어려운 문제는 아니었다 랭크에 쫄지말자
# 시간복잡도:(4*3*3*3 4방향이동 * (n-2)) * 2 * 10 공간복잡도:n**2m**2 방문처리때문
# .는 빈칸 #는 벽 0은 구멍
# import sys
# from collections import deque
# input = sys.stdin.readline
#
# # 한 방향씩 기울여야함
# move_type = [(-1, 0), (1, 0), (0, 1), (0, -1)]
# def move(direction, x, y):
#     count = 0
#     while True:
#         nx, ny = x + direction[0], y + direction[1]
#         if data[nx][ny] == '#':
#             return x, y, count, False
#         if data[nx][ny] == 'O':
#             return 0, 0, 0, True
#         x, y = nx, ny
#         count += 1
#
# # red, blue 구슬을 한번에 굴린다.
# def bfs():
#     global min_val, visited
#     rx, ry, bx, by = red_pos[0], red_pos[1], blue_pos[0], blue_pos[1]
#     q = deque([[rx, ry, bx, by, 0]])  # 0: count
#     visited[rx][ry][bx][by] = True
#
#     while q:
#         rx, ry, bx, by, count = q.popleft()
#         # if count > min_val: # 최적화 <- 필요가 없다, nr_result 값인 red 구슬이 첫번째로 들어갔을 때가 정답이고
#         # 바로 return 하면 됨, bfs의 특징
#         #     continue
#         if count >= 10:
#             return
#         for mv in move_type:
#             nrx, nry, nr_count, nr_result = move(mv, rx, ry)
#             nbx, nby, nb_count, nb_result = move(mv, bx, by)
#
#             if nb_result: #blue가 빠진경우 skip
#                 continue
#             if nr_result:
#                 min_val = min(min_val, count + 1)
#                 return
#             if nrx == nbx and nry == nby: # 좌표가 동일하고
#                 if nr_count < nb_count: # 더 멀리서 온 경우 한칸 전으로 이동
#                     nbx, nby = nbx - mv[0], nby - mv[1]
#                 else:
#                     nrx, nry = nrx - mv[0], nry - mv[1]
#
#             if not visited[nrx][nry][nbx][nby]:
#                 q.append((nrx,nry,nbx,nby,count + 1))
#                 visited[nrx][nry][nbx][nby] = True
#
#
# n, m = map(int, input().split())
# data = []
# red_pos, blue_pos = (0, 0), (0, 0)
# # visited = [[[False] * m for _ in range(n)] * m for _ in range(n)] 틀림, 유의
# visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
#
# for i in range(n):
#     line = list(input().rstrip())
#     data.append(line)
#     for j in range(m):
#         if line[j] == 'R':
#             red_pos = (i, j)
#         elif line[j] == 'B':
#             blue_pos = (i, j)
# min_val = int(1e9)
# bfs()
# print(min_val if min_val != int(1e9) else -1)

# 9. 연구소
# 3개를 설치하는 모든 경우의 수
# 바이러스 위치 저장, bfs
# 최대 8*8
# 시간복잡도: (64C3) * (nm) bfs
# 정~~~말 잘했다 시간소요 300ms 인데 랭킹 29등이야!!
# 백트래킹으로도 3개를 설치하는 모든 경우의수 계산이 가능하네
# from itertools import combinations
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# INF = int(1e9)
# n, m = map(int, input().split())
# visited = [[0] * m for _ in range(n)]
# visited_num = 0
# data = []  # 0 빈칸, 1 벽, 2 바이러스
# virus = []
# empty = [] # 빈칸 위치 저장
# wall_cnt = 3 # 3개 추가되기 때문
# for i in range(n):
#     row = list(map(int, input().rstrip().split()))
#     for j in range(len(row)):
#         if row[j] == 2:
#             virus.append((i, j))
#         elif row[j] == 0:
#             empty.append(m * i + j)  # 빈칸의 위치는 0 ~ nm 형태로 나타냄
#         else:
#             wall_cnt += 1
#     data.append(row)
#
# move_type = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#
#
# def bfs():
#     global visited_num, max_val
#     visited_num += 1
#     q = deque(virus)
#     count = len(virus)
#
#     while q:
#         x, y = q.popleft()
#         for move in move_type:
#             nx, ny = x + move[0], y + move[1]
#             if point_validator(nx, ny):
#                 q.append((nx, ny))
#                 visited[nx][ny] = visited_num
#                 count += 1
#     max_val = max(max_val, n * m - count - wall_cnt)
#
#
# def point_validator(x, y):
#     if x < 0 or y < 0 or x >= n or y >= m:
#         return False
#     if visited[x][y] == visited_num or data[x][y] != 0:
#         return False
#     return True
#
#
# max_val = 0
# # 빈칸에서 벽 3개를 설치하는 모든 경우의 수
# for case in combinations(empty, 3):
#     for c in case:
#         data[c // m][c % m] = 1
#     bfs()
#     for c in case:
#         data[c // m][c % m] = 0
#
# print(max_val)

# 10. 연산자 끼워넣기
# 백트래킹?
# n == 11 개면  연산자 모든 경우의수 10개
# 10개 중 10개 놓는 모든 경우의 수 10P10 /6 최소한 중복되는수
# 성공!

# import sys
# input = sys.stdin.readline
#
# n = int(input())
# num_list = list(map(int, input().rstrip().split()))
# op = list(map(int, input().rstrip().split())) # 덧셈, 뺄셈, 곱셈, 나눗셈
#
# def btk(depth, total, index):
#     global max_val, min_val
#
#     if depth == n - 1:
#         max_val = max(max_val, total)
#         min_val = min(min_val, total)
#         return
#
#     for i in range(4):
#         if op[i] > 0:
#             op[i] -= 1
#             if i == 0:
#                 temp = total + num_list[index]
#             if i == 1:
#                 temp = total - num_list[index]
#             if i == 2:
#                 temp = total * num_list[index]
#             if i == 3:
#                 if total < 0:
#                     temp = -(abs(total) // num_list[index])
#                 else:
#                     temp = total // num_list[index]
#             btk(depth + 1, temp, index + 1)
#             op[i] += 1
#
#
# min_val = int(1e9)+1
# max_val = int(-1e9)-1
# btk(0, num_list[0], 1)
# print(max_val)
# print(min_val)

# 11. 스타트와 링크
# 시간복잡도 20C10 * 10 -> 간신히 될거같은데
# 블로그 참조, 다시풀기
# import sys
# from itertools import combinations
# input = sys.stdin.readline
# n = int(input())
# data = [list(map(int, input().rstrip().split())) for _ in range(n)]
# data_total = sum(map(sum, data))
#
# def btk(comb, depth, total):
#     global result
#
#     if depth == n//2:
#         result = min(result, abs(total - abs(data_total - total)))
#         return
#
#     for k in range(n//2):
#         if k == depth:
#             continue
#         total = total + data[comb[depth]][comb[k]]
#     btk(comb, depth + 1, total)
#
#
# result = int(1e9)
# for comb in combinations(range(n), n//2):
#     btk(comb, 0, 0)
#     if result == 0:
#         print(result)
#         break
# print(result)


# 블로그참조
# 정말 쉽구나..
# 다시풀자
# 궁금하니 bfs 풀이도 한번 보자
# from itertools import combinations as c
#
# n = int(input())
# array = [i for i in range(n)]
# matrix = []
# for _ in range(n):
#     matrix.append((list(map(int, input().split()))))
# result = int(1e9)
# for r1 in c(array, n//2):
#     start, link = 0, 0
#     r2 = list(set(array) - set(r1))
#     for r in c(r1, 2):
#         start += matrix[r[0]][r[1]]
#         start += matrix[r[1]][r[0]]
#     for r in c(r2, 2):
#         link += matrix[r[0]][r[1]]
#         link += matrix[r[1]][r[0]]
#     result = min(result, abs(start-link))
# print(result)


# 12. 경사로
# 실패 다시풀기
# 문제점 1. 코드가 길어졌어
# 원인은? 구현을 어떻게 할지는 정하고 시작했는데
# 1. check 함수에서 매개변수 하나로 row, col 동시에 처리할순없을까 고민을 했었어야했어
# 2. while문보단 for 문을쓰는게 훨씬 깔끔해지고 편해져
# 급하다고 코드를 막 치지 말고 조금만 더 생각하면서 치자..
# 다시풀자

# import sys
# input = sys.stdin.readline
# ROW = 0
# COLUM = 1
#
# def check(x, y, direction):
#     if direction == ROW:
#         if x==0:
#             print(x)
#         build_point = []
#         while y < N-1:
#             if data[x][y] == data[x][y + 1]:
#                 y += 1
#                 continue
#             elif data[x][y] - data[x][y + 1] == 1: #높이 차이가1인경우 왼쪽이 더 높음
#                 if N - y >= L: #경사로 길이만큼 설치 가능 여부 확인
#                     temp = y
#                     if L == 1:
#                         if temp not in build_point:
#                             build_point.append(temp)
#                         else:
#                             return False
#                         y+=1
#                         continue
#
#                     for _ in range(L-1):
#                         if temp in build_point or (temp+1) in build_point:
#                             return False
#                         if data[x][temp] == data[x][temp + 1]:
#                             build_point.append(temp)
#                             temp += 1
#                         else:
#                             return False
#                     build_point.append(temp + 1)
#                 else:
#                     return False
#             elif data[x][y] - data[x][y + 1] == -1: #높이 차이가-1인경우 오른쪽이 더 높음
#                 if y >= L-1: #경사로 길이만큼 설치 가능 여부 확인
#                     temp = y
#                     if L == 1:
#                         if temp not in build_point:
#                             build_point.append(temp)
#                         else:
#                             return False
#                         y+=1
#                         continue
#
#                     for _ in range(L-1):
#                         if temp in build_point or (temp-1) in build_point:
#                             return False
#                         if data[x][temp] == data[x][temp-1]:
#                             build_point.append(temp)
#                             temp -= 1
#                         else:
#                             return False
#                     build_point.append(temp - 1)
#                 else:
#                     return False
#             else:
#                 return False
#             y += 1
#
#     elif direction == COLUM:
#         build_point = []
#         while x < N-1:
#             if data[x][y] == data[x + 1][y]:
#                 x += 1
#                 continue
#             elif data[x][y] - data[x + 1][y] == 1: #높이 차이가1인경우 왼쪽이 더 높음
#                 if N - x >= L: #경사로 길이만큼 설치 가능 여부 확인
#                     temp = x
#                     if L == 1:
#                         if temp not in build_point:
#                             build_point.append(temp)
#                         else:
#                             return False
#                         x+=1
#                         continue
#
#                     for _ in range(L-1):
#                         if temp in build_point or (temp+1) in build_point:
#                             return False
#                         if data[temp][y] == data[temp+1][y]:
#                             build_point.append(temp)
#                             temp += 1
#                         else:
#                             return False
#                     build_point.append(temp + 1)
#                 else:
#                     return False
#             elif data[x][y] - data[x+1][y] == -1: #높이 차이가-1인경우 오른쪽이 더 높음
#                 if x >= L-1: #경사로 길이만큼 설치 가능 여부 확인
#                     temp = x
#                     if L == 1:
#                         if temp not in build_point:
#                             build_point.append(temp)
#                         else:
#                             return False
#                         x+=1
#                         continue
#
#                     for _ in range(L-1):
#                         if temp in build_point or (temp-1) in build_point:
#                             return False
#                         if data[temp][y] == data[temp-1][y]:
#                             build_point.append(temp)
#                             temp -= 1
#                         else:
#                             return False
#                     build_point.append(temp - 1)
#                 else:
#                     return False
#             x += 1
#     return True
#
#
# N, L = map(int, input().rstrip().split())
# data = [list(map(int, input().rstrip().split())) for _ in range(N)]
# result = 0
# for i in range(N):
#     if check(i, 0, ROW):
#         print('row', i)
#         result += 1
#     if check(0, i, COLUM):
#         print('col',i)
#         result += 1
# print(result)

# 12. 경사로 재풀이
# 완료
# import sys
# input = sys.stdin.readline
#
# def check(arr):
#     build = [False] * N
#     for i in range(N-1):
#         if arr[i] == arr[i+1]:
#             continue
#         elif abs(arr[i] - arr[i + 1]) > 1:
#             return False
#         elif arr[i]-arr[i+1] == 1: # 좌측이 더 큰 경우 오른쪽에 배치
#             for j in range(i+1, i+1+L):
#                 if 0 <= j < N:
#                     if arr[i+1] == arr[j] and not build[j]: # 바닥이 평평한지 확인
#                         build[j] = True
#                     else:
#                         return False
#                 else:
#                     return False
#         elif arr[i]-arr[i+1] == -1: # 우측이 더 큰 경우 좌측에 배치
#             for j in range(i, i-L, -1):
#                 if 0 <= j < N:
#                     if arr[i] == arr[j] and not build[j]: # 바닥이 평평한지 확인
#                         build[j] = True
#                     else:
#                         return False
#                 else:
#                     return False
#     return True
#
# N, L = map(int, input().rstrip().split())
# data = [list(map(int, input().rstrip().split())) for _ in range(N)]
#
# result = 0
# for i in range(N):
#     if check(data[i]): # 행
#         result += 1
#
#     temp = []
#     for j in range(N):
#         temp.append(data[j][i])
#     if check(temp): # 열
#         result += 1
#
# print(result)


# 13. 사다리 조작
# 매우 매우 매우 어려웠다
# 사다리를 1개 놓은것, 2개놓은것, 3개놓은것 모두 확인
# 시간복잡독 2700C1*2700 + 2700C2*2700 + 2700C3*2700 이면 불가인데
# 완전탐색이 안먹히는거같은데..
# 블로그 참조
# 아.. 2700이 아니라 270이었어
# 270 이어도 안될것처럼 보이는데 최적화로 해결해야되나보다
# 270C3 * 270 (연결확인) 이면 13억
# 사다리는 true false로 만들자


# 콤비네이션을 그대로 쓰면 시간초과
# 시간초과 나지 않으려면 btk로 최적화해야함
# 블로그 참조 했음

# def check(depth):
#     for i in range(N):
#         now = i
#         for j in range(H):
#             if data[j][now]:
#                 now += 1
#             elif now > 0 and data[j][now -1]:
#                 now -= 1
#         if now != i:
#             return False
#     return True
#
#
# def btk(depth, x, y):
#     global result
#     if result <= depth:
#         return
#     if check(depth):
#         result = min(result, depth)
#     if depth == 3:
#         return
#
#     for i in range(x, H):
#         if i == x: #라인이 그대로면 y축 계속탐색
#             temp = y
#         else:
#             temp = 0# 라인이 바뀌면 0부터 다시 탐색
#         for j in range(temp, N-1):
#             if not data[i][j]:
#                 if j >= N-1 and data[i][j+1]:
#                     continue
#                 if j > 0 and data[i][j-1]:
#                     continue
#                 data[i][j] = True
#                 btk(depth + 1, i, j + 2)
#                 data[i][j] = False
#
# # 세로선, 가로선 갯수, 세로선마다 가로선의 갯수
# N, M, H = map(int, input().split())
# data = [[False] * N for _ in range(H)]
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     data[a-1][b-1] = True
#
# result = 4
# btk(0, 0, 0)
# print(result if result != 4 else -1)

# 14. 드래곤 커브
# 1. 시작점
# 2. 시작방향
# 3. 세대
# 1. 시작점에서 시작 방향으로 선분1을 긋는다
# 다음 세대는 오른쪽으로 90도 회전한것을 꼭지점에 붙인 것
# 이전 꼭지점과 회전 후 꼭지점 위치를 맞추면 드래곤커브를 붙일 수 있다.
# 결과: 모든 꼭지점이 드래곤 커브인것의 갯수
# 100, 100 만 유효한 좌표
# 드래곤커브는 겹칠 수 있다
# x,y 좌표, 방향, 세대(해당세대까지 진화)
# 각각의 드래곤 좌표를 기억해야할거같은데

# 블로그 참조하자
# 아래 풀이는 잘못됐다
# 회전을 어떻게할지 고민했는데 회전이 아닌 규칙성을 찾아야했다

# 구현 문제는 아이디어가 가장 중요하구나
# 아이디어 => 직접 그려보면 규칙성이 보임
# 참조 https://kyun2da.github.io/2021/04/06/dragonCurve/
# 이건 다시 풀어보자..


# def upgrade(index): # 회전 + 꼭지점에 붙인 좌표 return
#     before_x, before_y = dragon_pos[index] # 꼭지점
#     after_x, after_y = 0, 0
#     temp = [[0] * 100 for _ in range(100)]
#     pos = []
#     for i in range(100):
#         for j in range(100):
#             if data[i][j] == index:
#                 pos.append((j, 100 - i - 1))
#                 # temp[j][100-i-1] = data[i][j]
#                 if i == before_x and j == before_y:
#                     after_x = j
#                     after_y = 100 - i - 1
#
#     x_gap = before_x - after_x
#     y_gap = before_y - after_y
#
# n = int(input())
# data = [[0] * 100 for _ in range(100)]
# dragon = []
# dragon_pos = []
# move = [(0, 1), (-1, 0), (0, -1), (1, 0)]
# for i in range(n):
#     y, x, d, g = map(int, input().split())
#     dragon.append((x, y, d, g))
#     data[x][y] = i
#     data[x+move[d][0]][y+move[d][1]] = i
#     dragon_pos.append((x+move[d][0], y+move[d][1])) #꼭지점
#
#
# for i in range(len(dragon)):
#     g = dragon[i][3]  # 세대
#     while g > 0:
#         g -= 1
#         dragon_pos[i] = (upgrade(i))
#
# all_pos = []
# for i in range(len(dragon_pos)):


