# def solution(triangle):
#     length = len(triangle[-1])
#     dp = [[0] * length for _ in range(length)]
#     dp[0][0] = triangle[0][0]
#
#     for i in range(1, len(triangle)):
#         for j in range(len(triangle[i])):
#             if j == 0:
#                 dp[i][j] = dp[i-1][j] + triangle[i][j]
#             elif j == len(triangle[i])-1:
#                 dp[i][j] = dp[i-1][j-1] + triangle[i][j]
#             else:
#                 dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
#     answer = max(map(max, dp))
#     return answer
#
# v = solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
# print(v)

# 좀 더 나은 풀이
def solution(triangle):
    dp = []
    for t in range(1, len(triangle)):
        for i in range(t+1):
            if i == 0:
                triangle[t][0] += triangle[t-1][0]
            elif i == t:
                triangle[t][-1] += triangle[t-1][-1]
            else:
                triangle[t][i] += max(triangle[t-1][i-1], triangle[t-1][i])
    return max(triangle[-1])