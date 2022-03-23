# 문제3 계단 오르기
n = int(input())
data = [None]
for _ in range(n):
    data.append(int(input()))

if n == 1:
    print(data[1])
    exit(0)
# 각 계단의 최댓값인 아래 테이블로 잡으면
# 세칸을 연속 밟는 경우에대해 고려할 수 없다
# dp = [0] * (n + 1)

# dp[i][j] 형태 i = 현재계단의 위치 j = 연속으로 밟은 계단의 수 (j 값의 경우 최대 2를 넘지 않는다)
dp = [[0] * 3 for i in range(n + 1)]

# 초깃값 설정
dp[1][1] = data[1]
dp[1][2] = 0
dp[2][1] = data[2]
dp[2][2] = data[1] + data[2]

for i in range(3, n + 1):
    dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + data[i]
    dp[i][2] = dp[i-1][1] + data[i]

print(max(dp[n][1], dp[n][2]))


# 문제3 계단 오르기 1차원 배열로 풀기
n = int(input())
data = [0]
for _ in range(n):
    data.append(int(input()))

if n == 1 :
    print(data[1])
    exit()
elif n == 2:
    print(data[1] + data[2])
    exit()

# dp 테이블 정의: dp[i] 의 경우 i 지점까지 계단을 밟지 않는 최솟값, 단 i 지점은 밟지 않아야함
dp = [0] * (n + 1)

dp[1] = data[1]
dp[2] = data[2]
dp[3] = data[3]

for i in range(3, n + 1):
    dp[i] = data[i] + min(dp[i-2], dp[i-3])

print(sum(data) - min(dp[n-1],dp[n-2]))

# 문제3 계단 오르기 문제푸는방식3
# dp 테이블 정의: n 번째 계단 까지의 최댓값, 단, n번째 계단은 꼭 밟아야함
n = int(input())
data = [0]
for _ in range(n):
    data.append(int(input()))

if n == 1:
    print(data[1])
    exit(0)
elif n == 2:
    print(data[1] + data[2])
    exit(0)

dp = [0] * (n + 1)
dp[1] = data[1]
dp[2] = data[1] + data[2]
dp[3] = max(data[1], data[2]) + data[3]

for i in range(3, n + 1):
    dp[i] = max(dp[i-2] + data[i], dp[i-3] + data[i-1] + data[i])

print(dp[n])