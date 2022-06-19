N = int(input())
dp = [0] * (N+1)

for i in range(2, N+1):
    mv = dp[i-1] + 1
    if i % 2 == 0:
        mv = min(mv, dp[i // 2] + 1)
    if i % 3 == 0:
        mv = min(mv, dp[i // 3] + 1)
    dp[i] = mv

print(dp[N])
