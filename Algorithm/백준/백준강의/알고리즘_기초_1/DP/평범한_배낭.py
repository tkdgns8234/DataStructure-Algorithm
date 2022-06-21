# 냅색 유형문제
# dp테이블 정의: dp[i][j]  : i까지 사용, j 무게까지의 최댓값
# 점화식: dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v), w는 i번째 무게 v 는 i번째 가치

N, K = map(int, input().split())
dp = [[0] * (K+1) for _ in range(N+1)]
data = [list(map(int, input().split())) for _ in range(N)]
data.sort(key=lambda x:x[0])

for i in range(1, len(data)+1):
    w, v = data[i - 1][0], data[i - 1][1]
    for j in range(K+1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp[N][K])