# dp[][1]에 경로를 담고
# 마지막 과 첫번째 값만 겹치지 않도록 처리해보려했는데
# 실패

def solution(money):
    dp = [[0,[]] for _ in range((len(money)+3))]

    for i in range(3, len(dp)):
        if dp[i-2][0] > dp[i-3][0]:
            dp[i][0] = dp[i-2][0] + money[i-3]
            dp[i][1] = dp[i-2][1] + [i]
        else:
            dp[i][0] = dp[i-3][0] + money[i-3]
            dp[i][1] = dp[i-3][1] + [i]

        if i == len(dp)-1:
            if dp[i - 2][0] > dp[i - 3][0]:
                if 3 in dp[i-2][1]:
                    dp[i][0] = dp[i - 2][0] + money[i - 3] - money[0]
            else:
                if 3 in dp[i-3][1]:
                    dp[i][0] = dp[i - 3][0] + money[i - 3] - money[0]
    return max(dp)[0]

v= solution([1,2,3,1])
print(v)



# 나중에 다시 풀자 신중히 풀면 그리 어렵지 않은 문제다.
# 블로그 참조
# https://velog.io/@imacoolgirlyo/프로그래머스-도둑질-파이썬

# 우선 위 풀이는 dp테이블을 정확히 정의하지도 않고 풀었다.. 따라서 점화식도 틀렸다.
# dp 테이블 정의부터 잘 해야한다
# dp테이블: dp[i] 까지의 이웃집을 털지 않는 최댓값
# 점화식: dp[i] = max(dp[i-1], dp[i-2]+now)
# 원형으로 되어있기 때문에 마지막 집을 털지 않는 경우와
# 첫번째 집을 털지 않는 두가지 경우 모두 돌려서 max 값을 출력하면 된다.


def solution(money):
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])

    for i in range(2, len(money)-1): # 마지막집을 털지 않는 경우
        dp1[i] = max(dp1[i-1], money[i]+dp1[i-2])

    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(2, len(money)): # 첫번째 집을 털지 않는 경우
        dp2[i] = max(dp2[i-1], money[i]+dp2[i-2])

    return max(max(dp1), max(dp2)) # 두 경우 중 최대