dp = [0] * 12
for T in range(int(input())):
    N = int(input())
    dp[1], dp[2], dp[3] = 1, 2, 4

    if N < 4:
        print(dp[N])
    else:
        for i in range(4, N+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        print(dp[N])