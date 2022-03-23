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


import sys
import copy

n = int(input())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = 0

rotate_now = 0

def rotate(m):
    global arr
    global rotate_now
    x = len(arr)
    y = len(arr[0])
    temp = [[0] * x for _ in range(y)]

    start = -1
    while start < m:
        for i in range(x):
            for j in range(y):
                temp[j][x - i - 1] = arr[i][j]
        start += 1
        arr = copy.deepcopy(temp)
    return

def move(idx):
    rotate(idx)
    # 0부터 3까지 상,하,좌,우 를 의미
    for i in range(n):
        idx = 0
        for j in range(1, n):
            if arr[i][j]:
                temp = arr[i][j]
                arr[i][j] = 0
                if arr[i][idx] == 0:
                    arr[i][idx] = temp
                elif arr[i][idx] == temp:
                    arr[i][idx] = temp * 2
                    idx += 1
                else:
                    idx += 1
                    arr[i][idx] = temp


def dfs(count):
    global ans, arr
    if count == 5:
        for i in range(n):
            ans = max(ans, max(arr[i]))
        return

    tmp = copy.deepcopy(arr)
    for i in range(4):
        move(i)
        dfs(count + 1)
        arr = copy.deepcopy(tmp)


dfs(0)
print(ans)