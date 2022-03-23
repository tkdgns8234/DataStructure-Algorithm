# 문제4 RGB 거리
# 와!!! 한방에 풀었어 너무 짜맀하다 ㅋㅋㅋㅋㅋㅋㅋ
# dp에 적응해가고있어
n = int(input())
dp = [[0] * 3 for i in range(n)]

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

# dp 테이블 = dp[i][j] i번째 j를 선택했을 때 모든 선택에 대한 최솟값
dp[0][0] = data[0][0]
dp[0][1] = data[0][1]
dp[0][2] = data[0][2]

for i in range(1, n):
    # dp[n][0]번째를 고른경우 dp[n-1][1], dp[n-1][3]의 최솟값 만 알면 됨
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + data[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + data[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + data[i][2]

print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))