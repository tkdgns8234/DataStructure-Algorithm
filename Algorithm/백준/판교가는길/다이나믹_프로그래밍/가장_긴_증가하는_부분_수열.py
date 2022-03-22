# dp 테이블: dp[i], i를 마지막 값으로 가지는 가장 긴 증가하는 부분 수열
# i번째 이하의 j 요소들을 모두 확인 하면서 dp[i]값을 업데이트 하는 방식
# 점화식: dp[i] = max(dp[i], dp[j]+1) if dp[j] < dp[i]

N = int(input())
data = list(map(int, input().split()))
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j]+1)

# print(dp[N-1])
print(max(dp))