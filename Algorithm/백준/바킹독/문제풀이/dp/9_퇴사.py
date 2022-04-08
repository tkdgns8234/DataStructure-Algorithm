# 9. 퇴사
# dp 테이블 정의를 앞에서부터 세우려고하면 세워지지 않는다
# 뒤에서부터 계산해보자
# 블로그 참조했음, 다시풀자
# n = int(input())
# data = [list(map(int, input().split())) for _ in range(n)]
# dp = [0] * (n + 1)
# for i in range(n-1, -1, -1):
#     if data[i][0] + i > n:
#         dp[i] = dp[i+1]
#     else:
#         dp[i] = max(dp[i+1], data[i][1] + dp[i + data[i][0]])
#
# print(dp[0])

# 다시 풀기
import sys
input = sys.stdin.readline
N = int(input())
T, P = [None], [None]
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (N + 2)
for i in range(N, 0, -1):
    if i + T[i] - 1 <= N:
        dp[i] = max(dp[i+1], P[i] + dp[i+T[i]])
    else:
        dp[i] = dp[i+1]

print(dp[1])