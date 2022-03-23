# 문제6 구간 합 구하기4
# # 구간의 합을 미리 계산해놓는 문제 prefix sum 이라고 지칭한다
n, m = map(int, input().split())
data = list(map(int, input().split()))
# dp 테이블 정의: dp[n] = 1번째 부터 n 번째까지의 합
dp = [0] * 100001
# 초깃값 설정
dp[1] = data[0]
# n번 만의 연산으로 1부터 n 까지의 구간 합을 모두 구할 수 있다
for i in range(2, n + 1):
    dp[i] = dp[i-1] + data[i-1]

result = []
for i in range(m):
    s, e = map(int, input().split())
    result.append(dp[e] - dp[s-1])

for r in result:
    print(r)