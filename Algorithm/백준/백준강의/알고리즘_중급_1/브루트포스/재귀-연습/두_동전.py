# 문제 요약
# bfs, 두 동전을 동시에 처리해야하는 문제
# 하나의 동전이 떨어지면 끝
# 벽이면 이동 불가, 동전자리는 이동 가능
# 하나의 동전만 떨어뜨리기위해 눌러야하는 버튼의 최소 횟수 출력
# 10 이상, 떨어뜨릴수없으면 -> -1 출력,

# 어려웠던점
# 1. point_validator 를 만들어 처리했는데
# 1-1. 조건을 잘 설정하지 못해서 다른 풀이를 참고햇다..
# 1-2. 따로 함수로 뺴서 처리하니 더 복잡해진 느낌이다. -> 개선

# 2. 60퍼에서 자꾸 틀린다.. 이유를 모르겠어
# ->    if dist > 10: 부분이 잘못됐었다.
# 범위 처리의 번거로움때문에 밑에서 dist + 1 로 return 하도록 했는데
# dist + 1 위치를 반환하기때문에 조건을 이상(>=)으로 설정해 주어야한다.

from collections import deque

def bfs(coins_point):
    global visited
    q = deque([[coins_point[0][0], coins_point[0][1], coins_point[1][0], coins_point[1][1], 0]])
    visited[coins_point[0][0]][coins_point[0][1]][coins_point[1][0]][coins_point[1][1]] = True
    while q:
        x1, y1, x2, y2, dist = q.popleft()
        if dist >= 10:
            return -1
        move_type = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for move in move_type:
            nx1, ny1, nx2, ny2 = x1+move[0], y1+move[1], x2+move[0], y2+move[1]
            if 0 <= nx1 < n and 0<= ny1 < m and 0 <= nx2 < n and 0<= ny2 < m:
                if board[nx1][ny1] == '#':
                    nx1, ny1 = x1, y1
                if board[nx2][ny2] == '#':
                    nx2, ny2 = x2, y2
                if not visited[nx1][ny1][nx2][ny2]:
                    visited[nx1][ny1][nx2][ny2] = True
                    q.append((nx1, ny1, nx2, ny2, dist+1))
            elif 0 <= nx1 < n and 0<= ny1 < m:
                return dist + 1
            elif 0 <= nx2 < n and 0<= ny2 < m:
                return dist + 1
            else:
                continue
    return -1

n, m = map(int, input().split())

board = []
coins_point = []
for i in range(n):
    temp = list(input())
    for j in range(len(temp)):
        if temp[j] == 'o':
            coins_point.append((i, j))
    board.append(temp)
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

print(bfs(coins_point))



# 다른 코드 참조
# from collections import deque
# import sys
#
# input = sys.stdin.readline
#
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
#
# def bfs():
#     while coin:
#         x1, y1, x2, y2, cnt = coin.popleft()
#
#         if cnt >= 10:
#             return -1
#
#         for i in range(4):
#             nx1 = x1 + dx[i]
#             ny1 = y1 + dy[i]
#             nx2 = x2 + dx[i]
#             ny2 = y2 + dy[i]
#
#             if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m:
#                 # 벽이라면
#                 if board[nx1][ny1] == "#":
#                     nx1, ny1 = x1, y1
#                 if board[nx2][ny2] == "#":
#                     nx2, ny2 = x2, y2
#                 coin.append((nx1, ny1, nx2, ny2, cnt + 1))
#             elif 0 <= nx1 < n and 0 <= ny1 < m:  # coin2가 떨어진 경우
#                 return cnt + 1
#             elif 0 <= nx2 < n and 0 <= ny2 < m:  # coin1가 떨어진 경우
#                 return cnt + 1
#             else:  # 둘 다 빠진 경우 무시
#                 continue
#
#     return -1
#
#
# if __name__ == "__main__":
#     n, m = map(int, input().split())
#
#     coin = deque()
#     board = []
#     temp = []
#     for i in range(n):
#         board.append(list(input().strip()))
#         for j in range(m):
#             if board[i][j] == "o":
#                 temp.append((i, j))
#
#     coin.append((temp[0][0], temp[0][1], temp[1][0], temp[1][1], 0))
#
#     print(bfs())


# 좋은 코드
# 보드 가장자리에 0을 추가해서 좌표의 보드값이 0일 때 떨어진것으로 간주
# 좋은 점: 범위를 처리할 필요 없음 (가장자리 이상을 움직이지 않음)
# 거리 또한 map 내부에서 처리
from collections import deque

dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]
def sol():
    while q:
        x1, y1, x2, y2 = q.popleft()
        if ck[x1][y1][x2][y2] > 10: break
        for i in range(4):
            xx1, yy1 = x1+dx[i], y1+dy[i]
            xx2, yy2 = x2+dx[i], y2+dy[i]
            if Map[xx1][yy1]==0 and Map[xx2][yy2]==0:
                continue
            if Map[xx1][yy1]==0: return ck[x1][y1][x2][y2]
            if Map[xx2][yy2]==0: return ck[x1][y1][x2][y2]
            if Map[xx1][yy1] == '#':
                xx1, yy1 = x1, y1
            if Map[xx2][yy2] == '#':
                xx2, yy2 = x2, y2
            if not ck[xx1][yy1][xx2][yy2]:
                ck[xx1][yy1][xx2][yy2] = ck[x1][y1][x2][y2]+1
                q.append([xx1, yy1, xx2, yy2])
    return -1

N, M = map(int, input().split(' '))
Map = [[0]*(M+2)]
for _ in range(N):
    Map.append([0]+list(input())+[0])
Map.append([0]*(M+2))
coin = []
for i in range(N+2):
    for j in range(M+2):
        if Map[i][j] == 'o':
            coin.append(i)
            coin.append(j)
            Map[i][j] = '.'
ck = [[[[0]*(M+2) for _ in range(N+2)] for _ in range(M+2)] for _ in range(N+2)]
ck[coin[0]][coin[1]][coin[2]][coin[3]] = 1
q = deque()
q.append([coin[0], coin[1], coin[2], coin[3]])
print(sol())