# LCS

# 2차원 dp 테이블을 만들어 풀 수 있는 문제
# 같은 알파벳인 경우 두 알파벳을 추가하기 전의 LCS 값에서 1을 더한 후 저장한다
# 다른 알파벳인 경우, 이전까지 비교한 값 중 최댓값을 구해야 한다.
# 이전까지 비교한 값 중 최댓값 => dp[n-1][j], dp[n][j-1]
s1 = input()
s2 = input()
len_s1 = len(s1)
len_s2 = len(s2)
dp = [[0] * (len_s2+1) for _ in range(len_s1+1)]

for i in range(1, len_s1+1):
    for j in range(1, len_s2+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j-1])

print(dp[len_s1][len_s2])
