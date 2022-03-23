# 문제1 1로 만들기
# # 10e6 이니 공간복잡도를 만족한다
n = int(input())
# # 해당 숫자가 되기 위한 최소 연산 횟수를 대입
dp = [0] * (n + 1)

dp[1] = 0

for i in range(2, n + 1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])