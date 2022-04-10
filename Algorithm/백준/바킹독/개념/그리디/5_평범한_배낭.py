# 문제5 평범한 배낭
# 그리디로 풀 수 있을거같지만 여러 반증을통해 그렇지 않다는걸 깨닳을 수 있다
# 이문제는 유명한 dp 유형의 문제이다
# 0-1 knapsack 문제로 분류된다 (물건을 분할할 수 없는경우)
# 상당히 어려운 문제다 풀이 패턴을 파악하고있어야만 나중에 비슷한 유형을 풀 수 있을것 같다
# 1. dp 테이블 정의
# dp[i][j] i: 물건의 종류 j = 가치 // 물건의 종류마다 가치에 해당하는 최댓값을 계속 업데이트 한다

n, k = map(int, input().split())
dp = [[0] * (k + 1) for i in range(n + 1)]

object = [(0, 0)]
for i in range(n):
    data = list(map(int, input().split()))
    object.append((data))

for i in range(1, n + 1):
    weight, value = object[i]
    for j in range(1, k + 1):
        if weight > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j])
print(dp[n][k])
# 반대로 쪼갤 수 있는 knapsack 알고리즘의 경우
# 그리디로 해결 가능하다
# 가치가 제일높은애들을 최대한 담고 공간이 부족하면
# 하나를 쪼개서 부분적으로 넣고 끝낸다
# 굳이 풀이를 하진 않겠다
