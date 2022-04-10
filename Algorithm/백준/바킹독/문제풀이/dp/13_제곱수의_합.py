import math
N = int(input())
dp = [i for i in range(100_001)]
for i in range(1, N+1):
    for now in range(1, int(math.sqrt(N)) + 1):
        if i - now**2 >= 0:
            dp[i] = min(dp[i], dp[i - now**2] + 1)
print(dp[N])
