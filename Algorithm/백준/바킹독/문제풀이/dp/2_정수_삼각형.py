# 2. 정수 삼각형
# 테이블 정의
# dp[i][j] i 번째에서  j를 선택했을 때 최댓값

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = data[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0: # 첫번째 줄
            dp[i][j] = dp[i-1][j] + data[i][j]
        elif j == i: # 마지막 줄
            dp[i][j] = dp[i-1][j-1] + data[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1] + data[i][j], dp[i-1][j] + data[i][j])

print(max(dp[n-1]))
