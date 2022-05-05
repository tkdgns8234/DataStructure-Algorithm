# target 제외하고 visit 처리
# 완전탐색방식은 4^10000 이므로 무조건 시간초과
# bfs로 최단거리를 탐색
# 타겟에 도착한 경우 방향 회전 횟수 기록
# 각각의 이동마다 현재 이동 방향, 회전 횟수를 기록
# 중복 방문을 어떻게 처리 해야할지가 좀 까다로웠다.
# 일반적인 방법으로 방문 처리를 하는경우 최소 거울의 수를 찾을 수 없다
# 차선책으로 각각의 위치마다 방문 가능한 횟수를 4번으로 제한해보았으나 해당 방법도 문제를 해결 할 수 없었다.
# 하여, 방문 처리를 해당 위치를 방문했을 때의 최소 방향전환 횟수로 설정하여
# 방향전환 수가 적은 노드만 방문할 수 있도록 설정하였다.

import sys
from collections import deque

def bfs(start):
    visited[start[0]][start[1]] = -1
    q = deque([start + [-1, -1]]) # 시작점, 이동방향, 방향 변환 횟수
    direct_cnt = []
    while q:
        x, y, direct, cnt = q.popleft()
        for d, move in enumerate([(0, -1), (0, 1), (-1, 0), (1, 0)]):
            nx, ny = x+move[0], y+move[1]
            if 0<=nx<N and 0<=ny<M and board[nx][ny] != '*':
                # 이동 방향이 일치하는 경우
                next_cnt = cnt if d == direct else cnt + 1
                if visited[nx][ny] >= next_cnt:
                    visited[nx][ny] = next_cnt

                    if board[nx][ny] == 'C':
                        direct_cnt.append(next_cnt)
                    else:
                        q.append((nx, ny, d, next_cnt))
    return min(direct_cnt)


M, N = map(int, input().split())
visited = [[sys.maxsize] * M for i in range(N)]
board = []
for i in range(N):
    row = list(input())
    for j in range(len(row)):
        if row[j] == 'C':
            start = [i, j]
    board.append(row)

rs = bfs(start)
print(rs)



# 참신한 방법
# 한 방향으로 우선 쭉 이동하는 방법
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            ## 동 남 서 북 순서
            nx, ny = x + dx[i], y + dy[i]
            while True:
                ## 범위를 벗어난다
                if not (0 <= nx < n and 0 <= ny < m): break

                ## 벽을 만난다
                if board[nx][ny] == '*': break

                ## 지난 적 있는 곳인데, 지금 경로로는 너무 많은 거울이 필요해서 break
                if visited[nx][ny] < visited[x][y] + 1: break

                ## board업데이트, queue 추가
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                nx = nx + dx[i]
                ny = ny + dy[i]