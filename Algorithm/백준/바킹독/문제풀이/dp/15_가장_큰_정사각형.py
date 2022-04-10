# 15. 가장 큰 정사각형
# 모든 부분을 확인하려면 최악의경우 (1000*1000)^2 가 소요되니
# dp로 풀어야한다는 생각을 떠올려야한다
# 다시풀자

# dp[i][j] -> i, j 를 꼭지점으로 갖는 정사각형의 최대 크기

N, M = map(int, input().split())
dp = [list(map(int, input())) for _ in range(N)]
for i in range(1, N):
    for j in range(1, M):
        if dp[i][j] == 1: # 1인 경우에만 정사각형을 만들 수 있으므로
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

print(max(map(max, dp))**2)