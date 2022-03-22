N, K = map(int, input().split())
coins = [0] + [int(input()) for _ in range(N)]
dp = [10001] * (K+1)
dp[0] = 0

for i in range(1, N+1):
    for j in range(coins[i], K+1):
        dp[j] = min(dp[j-coins[i]]+1, dp[j])

if dp[K] == 10001:
    print(-1)
else:
    print(dp[K])