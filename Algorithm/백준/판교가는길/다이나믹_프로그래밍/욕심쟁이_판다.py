# 1. 판다의 시작지점 정하기
# 2. 최대한 많은 칸을 이동

# 1. bfs vs dfs 선택 기준
# -> 판다가 움직일 수 있는 최단 거리가 아니라 최장 거리를 구해야하기 때문에 dfs를 선택한다.
# 또한, dfs만 사용했을때는 시간초과가 발생하는데, 중복으로 탐색을 여러번 하기 때문이다.
#
# 2. 이를위해 dp를 같이 사용해야 하는데, dp를 같이 사용해야 할 때, dfs를 사용해야 함을 풀이를 떠올리다보면 알 수 있다.
# -> dfs를 통해 한번 방문한곳은 최대 움직임이 항상 저장된다.
# 중복으로 방문할 필요가 없다. 한번 방문한곳은 최대 거리가 저장된다.

#아래 두가지 코드가 있는데 두번째 코드가 더 이해하고, 다시 풀었을때 써내려가기에도 쉽다
# 내가 푼 코드는 세번째 코드 <- 이게 제일 이상적인 코드같다.

#
# from sys import setrecursionlimit
# setrecursionlimit(10**9)
#
# def dfs(i, j):
#     if visited[i][j] < 0: # 방문한적이 없으면 깊이를 탐색
#         visited[i][j] = 0
#         for d in range(4):
#             x, y = i+dx[d], j+dy[d]
#             if 0<=x<n and 0<=y<n and forest[i][j] < forest[x][y]:
#                 # 여기서 추가로 방문하게 되는 경우 (추가 방문할곳이 1곳에서 끝난다면 추가방문한곳이 1이되고
#                 # 추가 방문한곳 기준으로 1이되는 이유는
#                 # 추가 방문한 위치는 4면이 모두 더 작은 위치이기 때문에 자기 자신의 방문횟수인 1 이 되는것이다.
#                 # 돌아와서 현재 위치는 아래 +=1  식에의해 2가된다 (자동으로 최대거리가 계속 저장됨))
#                 visited[i][j] = max(visited[i][j], dfs(x, y))
#         visited[i][j] += 1
#     return visited[i][j] # 방문한적이 없으면 탐색후, 탐색된 깊이를 return하고, 방문한적이 있으면 기존에 구한 값을 return한다.
#
#
# n = int(input())
# forest = [list(map(int, input().split())) for _ in range(n)]
# visited = [[-1] * n for _ in range(n)]
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
# ans = 0
# for i in range(n):
#     for j in range(n):
#         ans = max(ans, dfs(i, j))
# print(ans)
#
#
#
#
# #-----------------------------
# #유사하지만 조금 다른 풀이
# import sys
#
# input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 6)
#
# n = int(input())
# board = [list(map(int, input().split())) for _ in range(n)]
# dp = [[-1] * n for _ in range(n)]
# move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# ans = 0
#
# def dfs(x, y):
#     if dp[x][y] == -1: # 방문한적이 없으면 깊이를 탐색
#         dp[x][y] = 0
#
#         for a, b in move:
#             dx = x + a;
#             dy = y + b
#             if n > dx >= 0 and n > dy >= 0 and board[dx][dy] > board[x][y]:
#                 # 여기서 추가로 방문하게 되는 경우 (추가 방문할곳이 1곳에서 끝난다면 추가방문한곳이 0이되고
#                 # 추가 방문한 곳에서 +1을 return하기때문에
#                 # 돌아와서 현재 위치는 1이된다.
#                 dp[x][y] = max(dp[x][y], dfs(dx, dy))
#
#     return dp[x][y] + 1 # 방문한적이 없으면 탐색후, 탐색된 깊이 + 1(자기자신)을 return하고, 방문한적이 있으면 기존에 구한 값 +1을 return 한다.
#
#
# for i in range(n):
#     for j in range(n):
#         ans = max(ans, dfs(i, j))
#
# print(ans)


# 다시 풀어보자
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * N for _ in range(N)]

move_type = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def dfs(x, y):
    if dp[x][y] == -1: # 방문한적이 없으면 깊이를 탐색한다
        dp[x][y] = 0

        for move in move_type:
            nx, ny = x+move[0], y+move[1]
            if 0<=nx<N and 0<=ny<N:
                if data[x][y] < data[nx][ny]:
                    # 여기서 추가로 방문하게 되는 경우 (추가 방문할 수 있는곳이 한곳에서 끝난다면 추가방문한곳의 DP값이 0이되고
                    # 해당 값을 return, 현재 위치에서 추가방문한곳을 방문할 수 있기때문에 아래 코드에서 dfs() + 1
                    # 돌아오면 현재 위치의 DP값은 1이된다.
                    dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)


    # 방문한적이 없으면 탐색 후, 탐색된 깊이를 return하고
    # 방문한적이 있으면 기존에 구한 값을 return 한다.
    return dp[x][y]


ans = 0
for i in range(N):
    for j in range(N):
        ans = max(ans, dfs(i, j))
print(ans+1) # 1은 자기 자신의 위치