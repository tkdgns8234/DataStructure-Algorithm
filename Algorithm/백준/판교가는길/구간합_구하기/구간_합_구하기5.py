# N, M = map(int, input().split())
# dp = [[0] * N for _ in range(N)]
# for i in range(N):
#     temp = list(map(int, input().split()))
#     for j in range(N):
#         if j == 0:
#             dp[i][j] = temp[j]  # 첫 열은 그대로 대입
#         else:
#             dp[i][j] = temp[j] + dp[i][j - 1]
#
# ans = []
# for _ in range(M):
#     x1, y1, x2, y2 = list(map(int, input().split()))
#     x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
#     s = 0
#     for i in range(x1, x2 + 1):  # x축
#         if y1 > 0:
#             s += dp[i][y2] - dp[i][y1 - 1]
#         else:
#             s += dp[i][y2]
#     ans.append(s)
# print(*ans, sep='\n')

# 개선버전

N, M = map(int, input().split())
# 계산상 편의를 위해 리스트의 각각 첫번째 행, 열을 0으로 초기화
data = [[0]*(N+1)]
for _ in range(N):
    temp = [0] + list(map(int, input().split()))
    data.append(temp)

# 가로 합
for i in range(N+1):
    for j in range(N):
        data[i][j + 1] = data[i][j] + data[i][j+1]

# 세로 합
for i in range(N):
    for j in range(N+1):
        data[i+1][j] = data[i][j] + data[i+1][j]

ans = []
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    v = data[x2][y2] - data[x1-1][y2] - data[x2][y1-1] + data[x1-1][y1-1]
    ans.append(v)
print(*ans, sep='\n')
