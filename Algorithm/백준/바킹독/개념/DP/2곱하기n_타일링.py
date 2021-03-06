# 문제5 2*n 타일링
# 테이블 정의
# dp[n] => n 번째까지 타일을 채우는 모든 방법의 수
# -> 알고보니 피보나치 수열과 동일한값. 초깃값 제외
# 타일링 문제
n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 2
for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
print(dp[n])