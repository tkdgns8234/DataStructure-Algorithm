# 실패, 시간초과 발생

# 추가로
# 처음엔 visit 처리에 밤 ,낮까지 추가했다.
# 너무 생각없이 밤, 낮까지 추가했어..
# 밤 낮은 관계없이 먼저 도착한 경우를 따져야한다.

#
# import sys
# from collections import deque
#
# input = sys.stdin.readline
# N, M, K = map(int, input().split())
# board = [list(map(int, input().rstrip())) for _ in range(N)]
# visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
# q = deque([[0, 0, 0, 0]])
# visited[0][0][0] = 1
# ans = -1
# while q:
#     x, y, wall, time = q.popleft()
#     if x == N-1 and y == M-1:
#         ans = visited[x][y][wall]
#         break
#
#     dist = visited[x][y][wall] + 1
#     # if is_wait: dist += 1
#
#     for move in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#         nx, ny = x+move[0], y+move[1]
#         if 0<=nx<N and 0<=ny<M:
#             # 낮인경우
#             if time == 0:
#                 # 벽인경우
#                 if board[nx][ny] == 1:
#                     if wall < K and not visited[nx][ny][wall+1]:
#                         visited[nx][ny][wall+1] = dist
#                         q.append([nx, ny, wall+1, 1])
#                 # 벽이 아닌경우
#                 else:
#                     if not visited[nx][ny][wall]:
#                         visited[nx][ny][wall] = dist
#                         q.append([nx, ny, wall, 1])
#             # 밤인경우
#             else:
#                 if board[nx][ny] == 0:
#                     if not visited[nx][ny][wall]:
#                         visited[nx][ny][wall] = dist
#                         q.append([nx, ny, wall, 0])
#                 # 가고자 하는 방향이 벽인경우, 낮에 현 위치를 방문하지 않았으면 쉬었다 방문할 수 있음
#                 else:
#                     # if not visited[x][y][wall]:
#                     visited[x][y][wall] = dist
#                     q.append([x, y, wall, 0])
#
# print(ans)


# 개선
# 쉬었다 가는 경우를 개선

import sys
from collections import deque

input = sys.stdin.readline
N, M, K = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
q = deque([[0, 0, 0, 0, 0]])
visited[0][0][0] = 1
ans = -1
while q:
    x, y, wall, time, is_wait = q.popleft()
    if x == 0 and y == 2:
        pass
    if x == N-1 and y == M-1:
        ans = visited[x][y][wall]
        break

    dist = visited[x][y][wall] + 1
    if is_wait: dist += 1

    for move in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x+move[0], y+move[1]
        if 0<=nx<N and 0<=ny<M:
            # 낮인경우
            if time == 0:
                # 벽인경우
                if board[nx][ny] == 1:
                    if wall < K and not visited[nx][ny][wall+1]:
                        visited[nx][ny][wall+1] = dist
                        q.append([nx, ny, wall+1, 1, 0])
                # 벽이 아닌경우
                else:
                    if not visited[nx][ny][wall]:
                        visited[nx][ny][wall] = dist
                        q.append([nx, ny, wall, 1, 0])
            # 밤인경우
            else:
                if board[nx][ny] == 0:
                    if not visited[nx][ny][wall]:
                        visited[nx][ny][wall] = dist
                        q.append([nx, ny, wall, 0, 0])
                # 가고자 하는 방향이 벽인경우, 낮에 현 위치를 방문하지 않았으면 쉬었다 방문할 수 있음
                else:
                    if board[nx][ny] == 1:
                        if wall < K and not visited[nx][ny][wall+1]:
                            q.append([x, y, wall, 0, 1])

print(ans)