# 성공 했는데,, 너무 코드가 지저분해;
# 리팩토링 하자

# # 검은 블록을 내려서 터칠 수 있는 블록 모형
# block32 = [
#     [[0, 1],
#      [0, 1],
#      [1, 1]],
#
#     [[1, 0],
#      [1, 0],
#      [1, 1]],
# ]
#
# block23 = [
#     [[1, 0, 0],
#     [1, 1, 1]],
#
#     [[0, 0, 1],
#      [1, 1, 1]],
#
#     [[0, 1, 0],
#      [1, 1, 1]],
# ]
#
# def check(x, y, board):
#     while x >= 0:
#         if board[x][y] != 0:
#             return False
#         x -= 1
#     return True
#
# def enable_bomb(i, j, board):
#
#     if i + 1 < N and j + 2 < N:
#         pivot = -1
#         for a in range(i, i+2):
#             for b in range(j, j+3):
#                 if board[a][b] != 0:
#                     pivot = max(pivot, board[a][b])
#
#         for block in block23:
#             matched_count = 0
#             for a in range(2):
#                 for b in range(3):
#                     if block[a][b] == 1 and board[i+a][j+b] == pivot:
#                         matched_count += 1
#
#             if matched_count == 4:
#                 for a in range(2):
#                     for b in range(3):
#                         if board[i+a][j+b] != pivot:
#                             if not check(i+a, j+b, board):
#                                 return False
#                 # 0으로 만들기
#                 for a in range(2):
#                     for b in range(3):
#                         board[i+a][j+b] = 0
#                 return True
#
#     if i + 2 < N and j + 1 < N:
#         pivot = -1
#         for a in range(i, i + 3):
#             for b in range(j, j + 2):
#                 if board[a][b] != 0:
#                     pivot = max(pivot, board[a][b])
#
#         for block in block32:
#             matched_count = 0
#             for a in range(3):
#                 for b in range(2):
#                     if block[a][b] == 1 and board[i+a][j+b] == pivot:
#                         matched_count += 1
#
#             if matched_count == 4:
#                 for a in range(3):
#                     for b in range(2):
#                         if board[i+a][j+b] != pivot:
#                             if not check(i+a, j+b, board):
#                                 return False
#                 # 0으로 만들기
#                 for a in range(3):
#                     for b in range(2):
#                         board[i+a][j+b] = 0
#                 return True
#     return False
#
# def solution(board):
#     global N
#     N = len(board)
#
#     answer = 0
#     while True:
#         cnt = 0
#         for i in range(N):
#             for j in range(N):
#                 if enable_bomb(i, j, board):
#                     cnt += 1
#         if cnt == 0:
#             break
#         answer += cnt
#
#     return answer
#
# N = 0
# v = solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]])
# print(v)


# 훨씬 쉽네 아래 기반으로 내 코드 리팩토링 좀 해보자
# https://developer-ellen.tistory.com/26
# def canFill(row, col):
#     for i in range(row):
#         if Board[i][col]:
#             return False
#     return True
#
# def find(row, col, h, w):
#     emptyCnt = 0
#     lastValue = -1
#
#     for r in range(row, row+h):
#         for c in range(col, col+w):
#             if Board[r][c] == 0:
#                 if canFill(r, c) == False:
#                     return False
#                 emptyCnt += 1
#
#                 if emptyCnt > 2:
#                     return False
#             else:
#                 if lastValue == -1:
#                     lastValue = Board[r][c]
#                 elif lastValue != Board[r][c]:
#                     return False
#     for r in range(row, row+h):
#         for c in range(col, col+w):
#             Board[r][c] = 0
#     return True
#
# Board = []
# def solution(board):
#     global Board
#     Board = board
#     n = len(board)
#     answer = 0
#     while True:
#         cnt = 0
#         for i in range(n):
#             for j in range(n):
#                 if i <= n-2 and j <= n-3 and find(i, j, 2, 3):
#                     cnt += 1
#                 elif i <= n-3 and j <= n-2 and find(i, j, 3, 2):
#                     cnt += 1
#         answer += cnt
#         if cnt == 0:
#             break
#     return answer



# 재풀이 버전
# # 검은 블록을 내려서 터칠 수 있는 블록 모형
block32 = [
    [[0, 1],
     [0, 1],
     [1, 1]],

    [[1, 0],
     [1, 0],
     [1, 1]],
]

block23 = [
    [[1, 0, 0],
    [1, 1, 1]],

    [[0, 0, 1],
     [1, 1, 1]],

    [[0, 1, 0],
     [1, 1, 1]],
]


def check(x, y):
    for i in range(x+1):
        if Board[i][y] != 0:
            return False
    return True

def enable_bomb(i, j, r, c, arr):
    pivot = -1
    for a in range(i, i+r):
        for b in range(j, j+c):
            if Board[a][b] != 0:
                pivot = max(pivot, Board[a][b])

    for block in arr:
        matched_count = 0
        for a in range(r):
            for b in range(c):
                if block[a][b] == 1 and Board[i+a][j+b] == pivot:
                    matched_count += 1

        if matched_count == 4:
            for a in range(r):
                for b in range(c):
                    if Board[i+a][j+b] != pivot:
                        if check(i+a, j+b) == False:
                            return False
            # 0으로 만들기
            for a in range(r):
                for b in range(c):
                    Board[i+a][j+b] = 0
            return True
    return False

def solution(board):
    global N, Board
    N = len(board)
    Board = board

    answer = 0
    while True:
        cnt = 0
        for i in range(N):
            for j in range(N):
                if i + 2 <= N and j + 3 <= N:
                    if enable_bomb(i, j, 2, 3, block23):
                        cnt += 1
                if i + 3 <= N and j + 2 <= N:
                    if enable_bomb(i, j, 3, 2, block32):
                        cnt += 1
        if cnt == 0:
            break
        answer += cnt
    return answer

N = 0
Board = []
v = solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]])
print(v)