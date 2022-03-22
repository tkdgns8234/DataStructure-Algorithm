# 백트래킹 + DP방식?
# 실패, 당연히 시간초과

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(int(1e5))
# N, M = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(N)]
# dp = [[[0] * 3 for _ in range(M)] for _ in range(N)]
# visited = [[False] * M for _ in range(N)]
#
# move = [(1, 0), (0, 1), (0, -1)]
# def btk(x, y, total):
#     if x == N-1 and y == M-1:
#         return
#
#     for i in range(3):
#         nx, ny = x+move[i][0], y+move[i][1]
#         if 0<=nx<N and 0<=ny<M:
#             if not visited[nx][ny]:
#                 if dp[nx][ny][i] < total + data[nx][ny]:
#                     dp[nx][ny][i] = total + data[nx][ny]
#                     visited[nx][ny] = True
#                     btk(nx, ny, total + data[nx][ny])
#                     visited[nx][ny] = False
#
# visited[0][0] = True
# btk(0, 0, data[0][0])
#
# print(max(dp[N-1][M-1]))



# 2차원 dp 풀이
# 아래는 풀이하는데 참고되는 블로그
# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=occidere&logNo=220808155184
# 처음엔 2차원배열식 백준 이동하기 문제처럼 풀려고했으나, 이동 방향이 한방향이 아니라 불가능하다 생각했다.
# 왜냐면 1,1 위치에서 오른쪽에서 들어오는 경우는 오른쪽값이 개선되지 않은 채로 들어가기 때문이다.
# 이를위해 양방향으로 처리해야하는데,
# 맨 윗줄은 예외적으로 오른쪽으로 이동해야만 그 위치에 도달할 수 있기에 따로처리한다.
# 나머지 줄은 좌측, 우측 양방향으로 이동하면서 최댓값을 찾는다
# 물론 모두 아래에서 내려오는것도 함께 고려한다
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
dp = [[-int(1e4)] * M for _ in range(N)]

# 첫줄 먼저 처리
dp[0][0] = data[0][0]
for j in range(1, M):
    dp[0][j] = dp[0][j-1] + data[0][j]

# 나머지 줄 처리
for i in range(1, N):
    temp = [[-int(1e4)]*M for _ in range(2)] # 일시저장temp[0][]: 왼오방향 temp[1][]: 오왼방향
    # 왼 -> 오
    temp[0][0] = dp[i-1][0] + data[i][0]
    for j in range(1, M):
        temp[0][j] = max(temp[0][j-1], dp[i-1][j]) + data[i][j]

    # 왼 <- 오
    temp[1][M-1] = dp[i-1][M-1] + data[i][M-1]
    for j in range(M-2, -1, -1):
        temp[1][j] = max(temp[1][j+1], dp[i-1][j]) + data[i][j]

    for k in range(M):
        dp[i][k] = max(temp[0][k], temp[1][k])

print(dp[N-1][M-1])