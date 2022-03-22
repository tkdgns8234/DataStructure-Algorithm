# 10이 대표적인 반례
# greedy 로는 풀이할 수 없으니 dp를 사용해야한다
# dp테이블: 정수 n의 최소 연산 횟수
# 점화식: dp[n] = min(dp[n/2],dp[n/3],dp[n-1]) + 1 나눗셈은 나누어 떨어질때만 고려

N = int(input())
dp = [0]*(N+1)
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2])
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3])

print(dp[N])