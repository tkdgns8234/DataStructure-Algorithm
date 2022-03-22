# 완전탐색을 수행할경우 물품의수 100가지이므로 물건을 넣는경우, 안넣는 경우로 계산하면
# 시간복잡도는 O(2^100) 으로 시간초과가 발생한다.
# greedy 를 이용한 풀이도 불가능하다 (무게대비 가치가 좋은것만 사용하는경우) 반례가 존재한다.
# dp 테이블 dp[n][m] 물건n까지 사용했을때 m무게의 최댓값
#

# N, K = map(int, input().split())
# dp = [[0] * (K+1) for _ in range(N+1)]
#
# knapsack = [(0, 0)] #무게, 가치
# for i in range(N):
#     w, v = map(int, input().split())
#     knapsack.append((w, v))
#
# # i 는 물건
# # j 는 가치
# for i in range(1, N+1):
#     w, v = knapsack[i][0], knapsack[i][1]
#     for j in range(1, K+1):
#         if j < w: #물건의 무게 보다 작으면
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = max(dp[i-1][j - w] + v, dp[i-1][j])
#
# print(dp[N][K])