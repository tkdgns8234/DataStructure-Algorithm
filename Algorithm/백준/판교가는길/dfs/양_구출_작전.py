# dp 형식을 같이 써야하나

N = int(input())
dp = [0] * (N + 1)
data = []
for i in range(N):
    data.append(list(input().split()))

for animal, count, move in sorted(data, key=lambda x:x[2]):
    if animal == 'W':
        dp[i + 2] = dp[int(move)] + int(count)
    else:
        dp[i + 2] = dp[int(move)]

ans = 0
for animal, count, move in data:
    if animal == 'S':
        ans += int(count) - dp[int(move)]
print(ans)