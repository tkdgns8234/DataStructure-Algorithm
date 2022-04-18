# bfs 유형 문제
# 이건 먹고 들어가야해
# 실패

# ctrl 이동 or 4방향 이동 or enter/notenter
# enter 누른 카드를 같이 큐에 삽입
# 방문처리는? enter 단위로 처리해야할거같긴한데
# enter 한 위치(a, b) 로 관리하자 in 이면 이미 방문한곳
# enter 를 통해 터친 갯수가 타겟갯수면 멈춤
# x, y, 이동횟수, enter목록, 터친 갯수

# 아 보면 볼수록 백트래킹 + dfs or bfs? 유형 같은데
# -> 완전탐색 + bfs 는 맞다

# from collections import deque
# move_type = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#
# def control_move(x, y, board, board_len):
#     l = []
#     for move in move_type:
#         nx, ny = x + move[0], y + move[1]
#         while True:
#             if nx < 0 or nx >= board_len or ny < 0 or ny >= board_len:
#                 break
#             if board[nx][ny] != 0:
#                 l.append((nx, ny))
#                 break
#             else:
#                 nx, ny = nx + move[0], ny + move[1]
#     return l
#
# def solution(board, r, c):
#     max_count = 0
#     for b in board:
#         for i in b:
#             if i != 0:
#                 max_count += 1
#
#     board_len = len(board)
#     start = [r, c, [(r,c)], 1] #세로위치, 가로위치, 방문위치, 연산 수
#     q = deque([start])
#     answer = 0
#
#     while q:
#         print(q)
#         r, c, e_l, count = q.popleft()
#
#         if len(e_l) % 2 == 0:
#             x1,y1, x2,y2 = e_l[-1][0], e_l[-1][1], e_l[-2][0], e_l[-2][1]
#             if board[x1][y1] == board[x2][y2]:
#                 if len(e_l) == max_count:
#                     answer = count
#                     break
#             else:
#                 list(e_l).pop(), list(e_l).pop()
#
#         for move in move_type:
#             nr, nc = r+move[0], c+move[1]
#             if 0 <= nr < board_len and 0 <= nc < board_len:
#                 if board[nr][nc] != 0:
#                     if (nr, nc) not in e_l:
#                         temp = e_l + [(nr, nc)]
#                         q.append([nr, nc, temp, count+2]) #이동, 엔터 = 2
#
#         for move in control_move(r, c, board, board_len):
#             nr, nc = move[0], move[1]
#             if 0 <= nr < board_len and 0 <= nc < board_len:
#                 if board[nr][nc] != 0:
#                     if (nr, nc) not in e_l:
#                         temp = e_l + [(nr, nc)]
#                         q.append([nr, nc, temp, count+2]) #이동, 엔터 = 2
#
#     return answer
#
# v = solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,0)
# print(v)


# 좋은 코드
# https://tiktaek.tistory.com/68
# 1. permu를 사용해 선택할 카드의 순서를 정한다 (카드 수가 적음)
# 2. 모든 경우에 대해 조작 순서가 가장 작은것을 선택한다.
# 각 카드는 두개이므로
# (1,2,3) 1->2->3 번 카드순으로 확인할 경우 1 -> 2-a가빠른지  1 -> 2-b가빠른지도 확인해야함
# bfs 의 경우 매 순간 ctrl move, normal move 를 동시에 해야함


from collections import defaultdict, deque
from itertools import permutations
from copy import deepcopy
def move_cost(board, start, end):   # 조작 횟수 Count
    if start==end: return 0
    queue, visit = deque([[start[0], start[1], 0]]), {start}
    while queue:                    # BFS
        x, y, c = queue.popleft()
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = x+dx, y+dy     # Normal move
            cx, cy = x, y
            while True:             # Ctrl + move
                cx, cy = cx+dx, cy+dy
                if not (0 <= cx <= 3 and 0 <= cy <= 3):
                    cx, cy = cx-dx, cy-dy
                    break
                elif board[cx][cy] != 0:
                    break

            if (nx, ny) == end or (cx, cy) == end:  # 도착 최단 경로
                return c+1

            if (0 <= nx <= 3 and 0 <= ny <= 3) and (nx, ny) not in visit:
                queue.append((nx, ny, c+1))
                visit.add((nx, ny))
            if (cx, cy) not in visit:
                queue.append((cx, cy, c+1))
                visit.add((cx, cy))

def cls_cost(board, cdict, curr, order, cost):
    if len(order)==0: return cost   # 모든 카드를 확인한 경우
    idx = order[0]+1                # 현재 선택해야할 카드의 종류

    # 현재위치에서 A1까지의 조작 횟수 + A1->A2까지의 조작 횟수 + 2(카드 선택)
    choice1 = move_cost(board, curr, cdict[idx][0]) + move_cost(board, cdict[idx][0], cdict[idx][1]) + 2
    choice2 = move_cost(board, curr, cdict[idx][1]) + move_cost(board, cdict[idx][1], cdict[idx][0]) + 2

    # 선택한 카드는 board에서 0으로 변경
    new_board = deepcopy(board)
    new_board[cdict[idx][0][0]][cdict[idx][0][1]] = 0
    new_board[cdict[idx][1][0]][cdict[idx][1][1]] = 0

    if choice1 < choice2:   # 적은 조작 횟수를 한 경우를 따라 재귀
        return cls_cost(new_board, cdict, cdict[idx][1], order[1:], cost + choice1)
    else:
        return cls_cost(new_board, cdict, cdict[idx][0], order[1:], cost + choice2)

def solution(board, r, c):
    answer = float('inf')
    cdict = defaultdict(list)
    for row in range(4):        # 카드의 종류에 따라 좌표 저장
        for col in range(4):
            num = board[row][col]
            if num != 0:
                cdict[num].append((row, col))

    for case in permutations(range(len(cdict)), len(cdict)):    # 완전 탐색
        print(case)
        answer = min(answer, cls_cost(board, cdict, (r, c), case, 0))

    return answer

v = solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,0)
print(v)
