# 7. 가장 긴 증가하는 부분 수열
# 이전 문제 경험으로인해 쉽게 풀었다.
# 나중에 다시 푸는게 좋을거같다

n = int(input())
data = list(map(int, input().split()))
dp = [1] * n # 이전 원소들이 모두 작은경우 1

for i in range(1, n):
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
