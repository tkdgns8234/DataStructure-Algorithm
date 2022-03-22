N = int(input())
data = list(map(int, input().split()))
dp = [1]*N

for i in range(1, N):
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
x = max(dp)

rs = []
for i in range(N-1, -1, -1):
    if dp[i] == x:
        rs.append(data[i])
        x -= 1

print(*list(reversed(rs)), sep=" ")
