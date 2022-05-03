# 모든 벽을 기준으로 빈 공간을 탐색한다면 최대 배열의 크기가 1000000이므로
# 시간 초과가 발생한다.
# 한번의 탐색으로 모든 벽의 빈 공간을 알 수 없을까? 라는 생각을 했지만
# 아이디어를 떠올리지 못했다.

# 다른 블로그를 참조하며 검색해 본 결과
# flood fill 알고리즘에 속하는 문제였다.
# flood fill 은
# 배열의 시작 위치에서 목표 색으로 연결된 모든 칸을 방문해서 대체 색으로 변경하는 알고리즘이다

# 현재 문제에선 빈 공간을 그룹으로 묶어 각각의 색(숫자)으로 색칠하고 (flood fill)
# 각각의 색깔(숫자) 마다 빈 공간의 갯수를 구해놓는 식으로 구현한다.
# 이를 위해 flood fill 을 위한 배열 하나,
# 색깔별 갯수를 위한 key : value 자료구조인 dict 자료구조를 사용한다.
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, list(input().rstrip()))) for _ in range(N)]
color_board = [[0]*M for _ in range(N)]
visit = [[False]* M for _ in range(N)]
D = dict()

# 그룹 별로 색칠
def fill(x, y, color):
    color_board[x][y] = color
    visit[x][y] = True
    q = deque([[x, y]])
    cnt = 1
    while q:
        x, y = q.popleft()
        for move in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = x + move[0], y+move[1]
            if 0 <= nx < N and 0 <= ny < M:
                if not visit[nx][ny] and board[nx][ny] == 0:
                    q.append((nx, ny))
                    visit[nx][ny] = True
                    color_board[nx][ny] = color
                    cnt += 1
    return cnt


color = 1
for i in range(N):
    for j in range(M):
        if not visit[i][j] and board[i][j] == 0:
            D[color] = fill(i, j, color)
            color += 1

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            # 4방향 확인
            colors = set()
            cnt = 1
            for move in [(-1, 0), (1, 0), (0 ,1), (0, -1)]:
                ni, nj = i+move[0], j+move[1]
                if 0<=ni<N and 0<=nj<M:
                    color = color_board[ni][nj]
                    if color != 0 and color not in colors:
                        colors.add(color)
                        cnt += D[color]
            board[i][j] = cnt % 10


for i in range(N):
    print(''.join(map(str, board[i])))

# 풀이 방법 링크
# https://data-flower.tistory.com/86