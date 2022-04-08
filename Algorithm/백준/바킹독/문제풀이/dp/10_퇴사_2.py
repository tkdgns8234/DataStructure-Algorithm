# 10. 퇴사2
# 위와 동일한 문제, 다른 풀이가 있네?
# 시간복잡도는 O(n)으로 동일해보이는데 한번 해보자
# 그리 좋은풀이같지가 않아 직관적이지 않고 어려워 위 풀이가 훨씬 더 좋아보여
n = int(input())
dp = [0] * (n+1)
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

m  = 0
for i in range(n):
    m = max(m, dp[i])
    if i + data[i][0] > n:
        continue
    else:
        dp[i+data[i][0]] = max(dp[i+data[i][0]], data[i][1] + m)

print(max(dp))