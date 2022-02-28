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
import sys
from collections import deque
input = sys.stdin.readline()
n, m = map(int, input().split())
data = []
red_pos, blue_pos = (0, 0), (0, 0)
visited = [False]
for i in range(n):
    line = list(input().rstrip())
    data.append(line)
    for j in range(m):
        if line[j] == 'R':
            red_pos = (i, j)
        elif line[j] == 'B':
            blue_pos = (i, j)

# 한 방향씩 기울여야함
move_type = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def move():
    pass

# red, blue 구슬을 한번에 굴린다.
def bfs():
    q = deque([red_pos[0], red_pos[1], blue_pos[0], blue_pos[1]])

    pass

bfs()