N = int(input())
data = [0] + list(map(int, input().split()))
# dp[n][m]  n 개의 카드 사용한 경우 m 번째 카드 갯수 까지의 최댓값
dp = [[0] * (N + 1) for _ in range(N + 1)]

for n in range(1, N+1):
    for m in range(n, N+1):
        dp[n][m] = max(dp[n-1][m], dp[m-n][m-n] + data[n], dp[n][m-n]+data[n])
print(dp[N][N])


# 2차원배열로 안풀어도 된다.
# 점화식
# dp[i]: i번째 카드까지 사용했을 때 최댓값
# k: k번째 카드를 의미 data: k번째 카드의 가치
# dp[i] = max(dp[i], dp[i-k] + data)
# 아래 풀이 참조

N = int(input())
p = [0] + list(map(int,input().split()))
dp = [0 for _ in range(N+1)]


for i in range(1,N+1):
    for k in range(1,i+1):
        dp[i] = max(dp[i], dp[i-k] + p[k])
print(dp[i])
