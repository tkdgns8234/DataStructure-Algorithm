# 훨씬 간결한 코드들이 많다.. 참고하자

# def check(x, y, place):
#     for idx, move in enumerate([(0, -1), (0, 1), (1, 0), (-1, 0)]):
#         nx, ny = x + move[0], y + move[1]
#         if 0 <= nx < 5 and 0 <= ny < 5:
#             if place[nx][ny] == 'P':
#                 return False
#
#     # 상하좌우 + 2칸에 사람 있는지 확인
#     move_1_step = [(0, -1), (0, 1), (1, 0), (-1, 0)] # 1 step
#     for idx, move in enumerate([(0, -2), (0, 2), (2, 0), (-2, 0)]): # 2 step
#         nx, ny = x + move[0], y + move[1]
#         if 0 <= nx < 5 and 0 <= ny < 5:
#             if place[nx][ny] == 'P':
#                 # 사이공간 (1 step 확인)
#                 n1x, n1y = x + move_1_step[idx][0], y + move_1_step[idx][1]
#                 if place[n1x][n1y] != 'X':
#                     return False
#
#     # 대각선 확인
#     for idx, move in enumerate([(-1, -1), (-1, 1), (1, -1), (1, 1)]):
#         nx, ny = x + move[0], y + move[1]
#         if 0 <= nx < 5 and 0 <= ny < 5:
#             if place[nx][ny] == 'P':
#                 # 사이공간 확인
#                 n1x, n1y = x+move[0], y
#                 n2x, n2y = x, y+move[1]
#                 if place[n1x][n1y] != 'X' or place[n2x][n2y] != 'X':
#                     return False
#     return True
#
#
#
#
# def solution(places):
#     answer = []
#     for place in places:
#         flag = True
#         for i in range(5):
#             # 행 단위 확인
#             for j in range(5):
#                 if place[i][j] == 'P':
#                     if check(i, j, place) == False:
#                         flag = False
#                         break
#             if not flag:
#                 break
#         answer.append(1 if flag else 0)
#
#     return answer
#
# v = solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
# print(v)

# 좋은풀이 1
# 경우의 수가 적으니 가능한 풀이
def check(place):
    for irow, row in enumerate(place):
        for icol, cell in enumerate(row):
            if cell != 'P':
                continue
            if irow != 4 and place[irow + 1][icol] == 'P':
                return 0
            if icol != 4 and place[irow][icol + 1] == 'P':
                return 0
            if irow < 3 and place[irow + 2][icol] == 'P' and place[irow + 1][icol] != 'X':
                return 0
            if icol < 3 and place[irow][icol + 2] == 'P' and place[irow][icol + 1] != 'X':
                return 0
            if irow != 4 and icol != 4 and place[irow + 1][icol + 1] == 'P' and (place[irow + 1][icol] != 'X' or place[irow][icol + 1] != 'X'):
                return 0
            if irow != 4 and icol != 0 and place[irow + 1][icol - 1] == 'P' and (place[irow + 1][icol] != 'X' or place[irow][icol - 1] != 'X'):
                return 0
    return 1

def solution(places):
    return [check(place) for place in places]


# 백트래킹유형
# 좀 난해하다.
def solution(places):
    result = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def f(i, j, cnt):
        nonlocal good
        if cnt >2 : return
        if -1<i<5 and -1<j<5:
            if graph[i][j] == 'X':
                return

            if cnt != 0 and graph[i][j] == 'P':
                good = 0
                return

            # 아래 한줄이 왜 추가되어있는거지?
            graph[i][j] = 'X'
            # 백트래킹 유형으로 풀었네, 맨해튼 거리가 2인걸 이용하면 아래와같이 for 문을 돌릴 수 있다.
            for w in range(4):
                ni = i+dx[w]
                nj = j+dy[w]
                f(ni, nj, cnt+1)

    for case in places:
        graph = [list(r) for r in case]
        good = 1
        for i in range(5):
            for j in range(5):
                if graph[i][j]=='P':
                    f(i,j,0)

        result.append(good)
    return result


# 좋은풀이 3
# 이 풀이가 제일 좋아보여
# 정말 좋은코드다
# np는 지양하더라도 나머지 q 돌리는 코드가 너무 좋다
import numpy as np

def isvalid(p):
    q = []

    p = np.array([list(x) for x in p])
    for y, x in zip(*np.where(p == 'P')):
        q.append((y, x, y, x, 0))    # (y, x, 시작'P'y, 시작'P'x, 거리)

    while q:
        y, x, sy, sx, d = q.pop(0)

        if d < 2:
            for ny, nx in [(y-1, x), (y, x+1), (y+1, x), (y, x-1)]:
                # (ny, nx) != (sy, sx): 시작지점을 거르는것도 중요
                if -1 < ny < 5 and -1 < nx < 5 and (ny, nx) != (sy, sx):
                    # 바로 옆칸이 P 인 경우 위반
                    if p[ny, nx] == 'P': return 0
                    # 바로 옆칸(맨해튼거리1)이 빈칸인데 그 다음칸이 P인 경우 위반
                    # 다른 말로하면 맨해튼거리1인 칸이 파티션이 아닌데 맨해튼거리 2인칸이 사람이면 위반
                    elif p[ny, nx] == 'O': q.append((ny, nx, sy, sx, d+1))

    return 1

def solution(places):
    return [isvalid(p) for p in places]
