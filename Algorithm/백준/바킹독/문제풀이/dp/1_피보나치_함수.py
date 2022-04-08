# 1. 피보나치 함수
# 작은 문제의 반복, dp로 해결 가능
# dp 테이블 = i 번째 호출 시, 0과 1의 호출 횟수
# 점화식 dp[i][] = dp[i-1][] + dp[i-2][]
# dp = [[-1] * 2 for _ in range(41)]
# # # 초깃값 설정
# dp[0][0] = 1
# dp[0][1] = 0
# dp[1][0] = 0
# dp[1][1] = 1
#
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     for i in range(2, n + 1):
#         if dp[i][0] == -1:
#             dp[i][0] = dp[i-1][0] + dp[i-2][0]
#             dp[i][1] = dp[i-1][1] + dp[i-2][1]
#     print(dp[n][0], dp[n][1])