# dfs+ 백트래킹으로 O(n^2) 에 끝날거같은데 시간 초과 느낌
# 밟은곳의 값이 더 작으면 retrun 하면되나 해보자
# 역시 시간초과.. 백트래킹 = 완전탐색이잖아 이게 될리가 없지 당연히 NM^2 일텐데
# import sys
# sys.setrecursionlimit(int(1e5))
# input = sys.stdin.readline
# N, M = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(N)]
# dp = [[0] * M for _ in range(N)]
#
# move_type = [(1, 0), (0, 1), (1, 1)]
# def btk(x, y, total):
#     global ans
#
#     if dp[x][y] > total:
#         return
#     else:
#         dp[x][y] = total
#
#     if x == N-1 and y == M-1:
#         ans = max(ans, total)
#         return
#
#     for move in move_type:
#         nx, ny = x+move[0], y+move[1]
#         if 0 <= nx < N and 0 <= ny < M:
#             btk(nx, ny, total + data[nx][ny])
#
# ans = 0
# btk(0,0, data[0][0])
# print(ans)

# 처음 혹시나 하고 생각했던 2차원배열 dp 문제였다
# 대부분 2차원배열 dp는 계산상 편의를 위해 0,0 부터가 아닌 1,1 좌표부터 시작한다
# 움직이는데 장애물이 없고, 우측 아래방향으로 일방적으로 이동하므로
# dfs, bfs식으로 움직일 필요가 없다. 점화식을 세우고 완전탐색 하듯이 dp테이블을 채우며 이동하면 된다.

N, M = map(int, input().split())
candy = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + candy[i-1][j-1]


print(dp[N][M])