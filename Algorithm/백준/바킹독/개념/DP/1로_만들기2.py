# 문제7 1로 만들기 2
# 아래 더 잘짠 코드 존재
n = int(input())
dp = [0] * (int(1e6) + 1)
load = [0] * (int(1e6) + 1)

dp[1] = 0
load[1] = 0

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    load[i] = i - 1

    if i % 2 == 0:
        if dp[i // 2] + 1 < dp[i]:
            dp[i] = dp[i // 2] + 1
            load[i] = i // 2

    if i % 3 == 0:
        if dp[i // 3] + 1 < dp[i]:
            dp[i] = dp[i // 3] + 1
            load[i] = i // 3

print(dp[n])
print(n, end=" ")
while True:
    if n == 1:
        break
    print(load[n], end=" ")
    n = load[n]


# 잘 짠 코드 list + 연산으로 해결
N = int(input())

result = [[0, []] for _ in range(N + 1)]  # [최솟값, 경로 리스트]
result[1][0] = 0  # 최솟값
result[1][1] = [1]  # 경로를 담을 리스트

for i in range(2, N + 1):

    # f(x-1) + 1
    result[i][0] = result[i - 1][0] + 1
    result[i][1] = result[i - 1][1] + [i]

    # f(x//3) + 1
    if i % 3 == 0 and result[i // 3][0] + 1 < result[i][0]:
        result[i][0] = result[i // 3][0] + 1
        result[i][1] = result[i // 3][1] + [i]

    # f(x//2) + 1
    if i % 2 == 0 and result[i // 2][0] + 1 < result[i][0]:
        result[i][0] = result[i // 2][0] + 1
        result[i][1] = result[i // 2][1] + [i]

print(result[N][0])
for i in result[N][1][::-1]:  # 뒤집은 뒤 출력
    print(i, end=' ')