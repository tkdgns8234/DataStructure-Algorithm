# 문제2 1, 2, 3 더하기
# n이 최대 11이기 때문에 백트래킹을 사용해도 되나
# 11p3 11의 3제곱정도의 시간소요
# dp를 이용해 풀어보자
# 규칙성을 잘 모르겠으면, 하나씩 직접 나열해보자

# dp 테이블 정 1, 2, 3 으로 나타낼수있는 갯수
dp = [0] * 12
# 초깃값 설정
dp[1] = 1
dp[2] = 2
dp[3] = 4

test_count = int(input())
test_case = []

for _ in range(test_count):
    n = int(input())
    test_case.append(n)

for i in range(4, max(test_case) + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for t in test_case:
    print(dp[t])
