# dp 형식으로 풀 수 있어보인다
# 점화식을 세우지 못하고 다른 풀이를 참조했다.
# sknapsack 문제와 매우 흡사한 유형의 문제이다
# 2차원 dp를 사용
# dp테이블: dp[n][m] 기관차 n 개를 이용할 때, m개의 객차까지 포함했을때의 최댓값
# 점화식은 2차원 dp 테이블을 그려보고 구하기
# k 는 기관차가끌 수 있는 객차의 수 s 는 구간합
# 점화식: dp[n][m] = max(dp[n][m-1], dp[n-1][m-k] + s[m] - s[m-k]
# 시복: 객차수가 N 개라고 했을 떄 기관차의 수 * 객차 수 O(3N)정도

N = int(input())
data = [0] + list(map(int, input().split()))
dp = [[0] * (N+1) for _ in range(4)]  #dp 계산상 편의를 위해 3이아닌 4 사용
K = int(input()) # 기관차가 끌 수 있는 객차의 수
S = [0] # 구간합
for i in range(1, N+1):
    S.append(S[i-1] + data[i])

for i in range(1, 4): # 운영하는 기관차의 수
    for j in range(i*K, N+1): # 객차
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-K] + S[j] - S[j-K])

print(dp[3][N])