T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    data = [[0] * M for _ in range(N)]

    inputs = list(map(int, input().split()))
    for i in range(N):
        for j in range(M):
            data[i][j] = inputs[i * M + j]

    dp = [[0] * M for _ in range(N)]
    for i in range(N):
        dp[i][0] = data[i][0]

    for col in range(1, M):
        for row in range(N):
            if row == 0:
                dp[row][col] = max(dp[row][col - 1], dp[row + 1][col - 1]) + data[row][col]
            elif row == N - 1:
                dp[row][col] = max(dp[row][col - 1], dp[row - 1][col - 1]) + data[row][col]
            else:
                dp[row][col] = max(dp[row][col - 1], dp[row + 1][col - 1], dp[row - 1][col - 1]) + data[row][col]

    result = 0
    for i in range(N):
        result = max(result, dp[i][M - 1])
    print(result)
