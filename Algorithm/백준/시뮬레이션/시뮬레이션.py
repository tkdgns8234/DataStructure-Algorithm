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

