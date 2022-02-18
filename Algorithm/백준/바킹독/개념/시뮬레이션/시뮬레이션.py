# # 문제1 감시
# # 못 풀었다
# # 감탄스럽다 아래 주소의 코드
# # #https://developer-ellen.tistory.com/53
# # 좌 우 상 하
# import copy
# n, m = map(int, input().split())
# cc_info = []
# data = []
#
# move_type = [(0, -1), (0, 1), (-1, 0), (1, 0)]
# cctv = [
#         [],
#         [[0], [1], [2], [3]],
#         [[0, 1], [2, 3]],
#         [[0, 3], [0, 2], [1, 3], [1, 2]],
#         [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
#         [[0, 1, 2, 3]]
#         ]
#
# for i in range(n):
#     l = list(map(int, input().split()))
#     data.append(l)
#     for j in range(m):
#         if l[j] in [1, 2, 3, 4, 5]:
#             cc_info.append((l[j], i, j))
#
#
# def fill(md, x, y, arr):
#     for i in md:
#         nx = x
#         ny = y
#         while True:
#             nx = nx + move_type[i][0]
#             ny = ny + move_type[i][1]
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 break
#             # 벽인 경우
#             if arr[nx][ny] == 6:
#                 break
#             if arr[nx][ny] == 0:
#                 arr[nx][ny] = 7 # 7 을 cctv가 바라본 지역으로 설정
#
#
# def dfs(depth, arr):
#     global min_val
#
#     if depth == len(cc_info):
#         count = 0
#         for i in range(len(arr)):
#             count += arr[i].count(0)
#         min_val = min(min_val, count)
#         return
#     mode, x, y = cc_info[depth]
#     for md in cctv[mode]:
#         temp = copy.deepcopy(arr)
#         fill(md, x, y, temp)
#         dfs(depth + 1, temp)
#
#
# min_val = int(1e9)
# dfs(0, data)
# print(min_val)

# 문제2 스티커 붙이기
# 아래는 그냥 runtime 에실행해보면 다 잘 되는데
# 백준에서 수행시 시간초과
# 다시풀자
# import copy
# import sys
# input = sys.stdin.readline
# # 스티커 회전
# def rotation(sticker, x, y):
#     # 직사각형인 경우 x, y 크기 교체 필요
#     temp = [[0] * x for _ in range(y)]
#     s_position = []
#     # 회전
#     for i in range(x):
#         for j in range(y):
#             temp[j][x - i - 1] = sticker[i][j]
#             if sticker[i][j] == 1:
#                 # 회전된 포지션 저장
#                 s_position.append((j, x - i - 1))
#
#     return temp, s_position
#
#
# def attach(sticker_position, startx, starty):
#     temp = copy.deepcopy(note)
#     result = True
#     for s in sticker_position:
#         nx = startx + s[0]
#         ny = starty + s[1]
#
#         if nx < 0 or ny < 0 or nx >= n or ny >= m:
#             result = False
#             break
#         if temp[nx][ny] == 1:
#             result = False
#             break
#         # 조건을 모두 만족 하면 스티커 부분 대입
#         temp[nx][ny] = 1
#
#     return temp, result
#
#
# n, m, k = map(int, input().split())
# note = [[0] * m for i in range(n)]
#
# for _ in range(k):
#     sticker = []
#     sticker_position = []
#     sx, sy = map(int, input().split())
#     for i in range(sx):
#         data = list(map(int, input().split()))
#         sticker.append(data)
#         for j in range(len(data)):
#             if data[j] == 1:
#                 # 스티커 좌표 더하기
#                 sticker_position.append((i, j))
#
#     rotation_cnt = 0
#     attached = False
#     while not attached:
#         if rotation_cnt == 4:
#             break
#         for i in range(n):
#             for j in range(m):
#                 # 해당 칸에 붙이기
#                 rs_arr, attached = attach(sticker_position, i, j)
#                 # 붙인 경우 멈추기
#                 if attached:
#                     break
#             if attached:
#                 break
#
#         if not attached:
#             sticker, sticker_position = rotation(sticker, sx, sy)
#             sx = len(sticker)
#             sy = len(sticker[0])
#             rotation_cnt += 1
#         else:
#             note = copy.deepcopy(rs_arr)
#             break
#
# # 스티커 붙은 칸의 수 출력
# cnt = 0
# for i in range(n):
#     cnt += note[i].count(1)
# print(cnt)

# 다시풀기
# 문제2 스티커 붙이기
# 키포인트
# 1 도형 회전 (직사각형까지 고려)
# 2 스티커를 붙일 수 있는지 확인하는 방법
# 3 스티커 크기가 계속 변하기때문에 스티커 크기를 구할 땐 항상 해당 배열의 크기를 직접 구하기

# def rotation(sticker):
#     x = len(sticker)
#     y = len(sticker[0])
#
#     temp = [[0] * x for _ in range(y)]  # 직사각형인 경우 x, y 크기 교체 필요
#     for i in range(x):
#         for j in range(y):
#             temp[j][x - i - 1] = sticker[i][j]
#     return temp
#
#
# def check(start_x, start_y):
#     for i in range(len(sticker)):
#         for j in range(len(sticker[0])):
#             if note[start_x + i][start_y + j] + sticker[i][j] > 1:
#                 return False
#     return True
#
#
# def attach(start_x, start_y):
#     global note
#     # 스티커 붙이기
#     for i in range(len(sticker)):
#         for j in range(len(sticker[0])):
#             if sticker[i][j] == 1:
#                 note[start_x + i][start_y + j] = sticker[i][j]
#
#
# n, m, k = map(int, input().split())
# note = [[0] * m for i in range(n)]
#
# for _ in range(k):
#     sticker = []
#     sx, sy = map(int, input().split())
#     for i in range(sx):
#         sticker.append(list(map(int, input().split())))
#
#     rotation_cnt = 0
#     chk = False
#     while rotation_cnt < 4:
#         # 붙일 수 있는지 확인
#         for i in range(n - len(sticker) + 1):
#             for j in range(m - len(sticker[0]) + 1):
#                 if check(i, j):
#                     attach(i, j)
#                     chk = True
#                     break
#             if chk:
#                 break
#         if chk:
#             break
#         else:
#             rotation_cnt += 1
#             sticker = rotation(sticker)
#
# # 스티커 붙은 칸의 수 출력
# cnt = 0
# for i in range(n):
#     cnt += note[i].count(1)
# print(cnt)

# 문제3 easy
# 아래 풀이로 풀었지만, 도저히 개선 방안이 떠오르지 않는다 (오답처리)
# 다른 코드를 참고해 다시 풀자
# 전략: itertools 로 중복가능 순서상관있는 수열을 구하는 ~ 를사용
# 4개(상하좌우) 중 5개를 뽑는 경우의수 저장 후
# 모든 case 실행, max 값 출력
# 코드는 백준에 제출 확인


# 재풀이
# 이동방향
# 0 1 2 3
# 상 하 좌 우

# import copy
#
# def move(direct):
#     global data
#     if direct == 0:
#         for j in range(n):
#             idx = 0
#             for i in range(1, n):
#                 if data[i][j]:
#                     temp = data[i][j]
#                     data[i][j] = 0
#                     if data[idx][j] == 0:
#                         data[idx][j] == temp
#                     elif data[idx][j] == temp:
#                         data[idx][j] = temp * 2
#                         idx += 1
#                     else:
#                         idx += 1
#                         data[idx][j] = temp
#     #...이어서
#
# max_val = 0
# def dfs(depth):
#     global data
#     global max_val
#     if depth == 5:
#         max_val = max(max_val, max(map(max, data)))
#         return
#
#     temp = copy.deepcopy(data)
#     for i in range(4):
#         move(i)
#         dfs(depth + 1)
#         data = copy.deepcopy(temp)
#
# n = int(input())
# data = [list(map(int, input().split())) for i in range(n)]
# dfs(0)
# print(max_val)

# 치킨 배달
# from itertools import combinations
# HOUSE = 1
# CHICKEN = 2
# n, m = map(int, input().split())
# house = []
# chicken = []
#
# for i in range(n):
#     data = list(map(int, input().split()))
#     for j in range(len(data)):
#         if data[j] == HOUSE:
#             house.append((i, j))
#         elif data[j] == CHICKEN:
#             chicken.append((i, j))
#
# candidates = list(combinations(chicken, m))
#
# def dis(candidate):
#     total = 0
#     for h in house:
#         min_val = int(1e9)
#         for c in candidate:
#             hx, hy = h
#             cx, cy = c
#             min_val = min(min_val, abs(hx-cx) + abs(hy-cy))
#         total += min_val
#     return total
#
# result = int(1e9)
# for candidate in candidates:
#     result = min(result, dis(candidate))
# print(result)
