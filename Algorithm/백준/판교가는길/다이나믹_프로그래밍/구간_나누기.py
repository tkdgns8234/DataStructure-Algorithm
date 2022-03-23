# 와 처음으로 못풀겠는 문제가 등장했다.ㅋㅋㅋㅋㅋ
# 심지어 풀이를 봐도 잘 이해가 안가
# 나중에.... 다시풀자

# 다음날
# dp
# (귀납적 사고와 유사)큰문제를통해 작은 문제를 해결할 수 있다는 믿음을 가지고 풀어나가는 문제 (top down)
# or 작은문제를통해 큰문제 해결 bottom up

# dp 테이블: n개까지 m개 구간의 최댓값 dp[n][m]
# -1 3 1 2 4 -1
# n번째를 포함하지 않을 때: dp[n][m] = dp[n-1][m]
# n번째를 포함할 때: dp[n][m] = dp[k-2][m-1] + S[i] - S[k-1] -> k가 어디여야 최댓값인지 알 수 없으니 loop
# 두개의 max값

# k의 범위: 0~i-1 까지

# 이문제는 좀 아닌거같아.,
# ㅋㅋㅋㅋㅋ 여기까지

# N, M = map(int, input().split())
# dp = [[-int(1e9)] * (M+1) for _ in range(N+1)]
# prefix_sum = [0] * (N+1)
# for i in range(1, N+1):
#     num = int(input())
#     prefix_sum[i] = prefix_sum[i-1] + num
#
# dp[1][1] = prefix_sum[1]
# for i in range(1, N+1):
#     for j in range(1, M+1):
#         dp[i][j] = dp[i-1][j]
#         for k in range(i - 2, 0, -1):
#             dp[i][j] = max(dp[i][j], dp[k][j-1] + prefix_sum[i] - prefix_sum[k])
#
#
# print(dp[N][M])