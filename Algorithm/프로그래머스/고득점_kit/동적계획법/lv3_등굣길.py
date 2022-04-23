# dfs? 2^100 이라 시간초과
# dfs + dp?

# 1. dfs 풀이 시간 초과
INF = int(1e9)

def solution(m, n, puddles):
    dp = [[INF] * m for _ in range(n)]

    answer = 0
    def dfs(i, j, depth):
        nonlocal answer
        if i == n-1 and j == m-1:
            if dp[i][j] >= depth:
                answer += 1

        for move in [(0, 1), (1, 0)]:
            ni, nj = i + move[0], j + move[1]
            if 0 <= ni < n and 0 <= nj < m:
                if dp[ni][nj] >= depth + 1 and [nj+1, ni+1] not in puddles:
                    dp[ni][nj] = depth + 1
                    dfs(ni, nj, depth + 1)
    dfs(0, 0, 0)
    return answer%1_000_000_007

v = solution(4, 3, [[2,2]])
print(v)

# 풀이 참고
# https://dev-note-97.tistory.com/141
# 아.. 그리 어렵지 않은 문제였다.
# 이전에도 비슷한 유형의 문제를 접했던적이 있었는데
# 다음부터 틀리지 말자
# 근데 위 블로그  풀이를 봐도
# 어떻게 저 방식이 최단거리임을 항상 보장할 수 있는건지 잘 이해가 안된다
# -> 되돌아 가는 경로를 포함하지 않기 때문에 도달하는 모든 경로가 최단경로 라고 한다
# -> 위로가는 움직임, 좌측으로 가는 움직임이 없기 떄문에 항상 최단경로를 보장하는구나!


# dp 테이블 dp[i][j] = dp[i-1][j] + dp[i][j-1]
# dp 풀이
# 여러모로 까다로운 문제다
# 1. 오른쪽, 아래쪽으로만 이동하기때문에 항상 최단거리를 보장한다는 것을 인지해야하고
# 2. point를 쉽게 처리하기위해 dp테이블 row, colum을 하나씩 더 추가해서 처리하는것
# 3. 웅덩이가 존재하는경우 dp 값을 0으로 설정하는것
# 4. 매번 1_000_000_007 값을 나눠주는것이 더 효율적인것
# 을 생각하며 풀어야 한다

def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                dp[i][j] = 0
                continue
            dp[i][j] = (dp[i-1][j]+dp[i][j-1])%1_000_000_007
    return dp[n][m]

v = solution(4, 3, [[2, 2]])
print(v)