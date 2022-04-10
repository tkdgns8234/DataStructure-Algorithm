# 14. 동전
# 실패
# 어디서 많이 본 문제같더라니 냅색(배낭) 알고리즘으로 불리우는 유형의 문제였다
# 각 단위별로 만들수 있는 모든 경우의수를 차근차근 더해나가는 방식
# 다시풀자

# 재 풀이
T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    dp = [0] * 10001
    dp[0] = 1

    for coin in coins:
        for i in range(coin, M+1):
            dp[i] = dp[i] + dp[i-coin]

    print(dp[M])
