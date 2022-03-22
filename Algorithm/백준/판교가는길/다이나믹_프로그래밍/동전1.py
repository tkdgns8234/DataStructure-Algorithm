# dp테이블: dp[n][m] n원까지 사용했을 때 m원이 되는 모든 경우의 수
# 점화식: 2차원 배열을 그리고 값을 대입하면서 만들었다 냅색유형과 비슷하다
# dp[n][m] = dp[n-1][m]+dp[n][m-동전의 값]
# 시간초과 발생 코드

N, K = map(int, input().split()) # N종류 합이K
dp = [[0] * (K+1) for _ in range(N+1)]
coins = [0] + [int(input()) for _ in range(N)]
coins.sort()

# 초깃값
for i in range(1, N+1):
    dp[i][0] = 1

for i in range(1, N+1):
    for j in range(1, K+1):
        if j < coins[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]

print(dp[N][K])

# 위 코드는 시간초과 코드
# 메모리 제한을 못봤다....
# dp 메모리만 해도 초과다 int형 4 바이트 * 100만
# 1차원 dp로 풀어야한다

N, K = map(int, input().split()) # N종류 합이K
dp = [0] * (K+1)
coins = [int(input()) for _ in range(N)]
coins.sort()
dp[0] = 1

for coin in coins:
    for j in range(coin, K+1):
        dp[j] = dp[j-coin] + dp[j]
print(dp[K])
