# 8. 파도반 수열
dp = [-1] * 101
dp[1],dp[2],dp[3],dp[4],dp[5] = 1,1,1,2,2

T = int(input())
for _ in range(T):
    n = int(input())
    for i in range(6, n + 1):
        if dp[i] == -1:
            dp[i] = dp[i-5] + dp[i-1]
    print(dp[n])
