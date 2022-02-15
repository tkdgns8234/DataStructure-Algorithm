# 1. dp 테이블 만들기
# 2. 점화식 세우기
# 3. 초기값 설정하기

# 문제1 1로 만들기
# # 10e6 이니 공간복잡도를 만족한다
# n = int(input())
# # 해당 숫자가 되기 위한 최소 연산 횟수를 대입
# dp = [0] * (n + 1)
#
# dp[1] = 0
#
# for i in range(2, n + 1):
#     dp[i] = dp[i-1] + 1
#     if i % 2 == 0:
#         dp[i] = min(dp[i], dp[i // 2] + 1)
#     if i % 3 == 0:
#         dp[i] = min(dp[i], dp[i // 3] + 1)
#
# print(dp[n])

# # 문제2 1, 2, 3 더하기
# # n이 최대 11이기 때문에 백트래킹을 사용해도 되나
# # 11p3 11의 3제곱정도의 시간소요
# # dp를 이용해 풀어보자
# # 규칙성을 잘 모르겠으면, 하나씩 직접 나열해보자
#
# # dp 테이블 정 1, 2, 3 으로 나타낼수있는 갯수
# dp = [0] * 12
# # 초깃값 설정
# dp[1] = 1
# dp[2] = 2
# dp[3] = 4
#
# test_count = int(input())
# test_case = []
#
# for _ in range(test_count):
#     n = int(input())
#     test_case.append(n)
#
# for i in range(4, max(test_case) + 1):
#     dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
#
# for t in test_case:
#     print(dp[t])



# 문제3 계단 오르기
# n = int(input())
# data = [None]
# for _ in range(n):
#     data.append(int(input()))
#
# if n == 1:
#     print(data[1])
#     exit(0)
# # 각 계단의 최댓값인 아래 테이블로 잡으면
# # 세칸을 연속 밟는 경우에대해 고려할 수 없다
# # dp = [0] * (n + 1)
#
# # dp[i][j] 형태 i = 현재계단의 위치 j = 연속으로 밟은 계단의 수 (j 값의 경우 최대 2를 넘지 않는다)
# dp = [[0] * 3 for i in range(n + 1)]
#
# # 초깃값 설정
# dp[1][1] = data[1]
# dp[1][2] = 0
# dp[2][1] = data[2]
# dp[2][2] = data[1] + data[2]
#
# for i in range(3, n + 1):
#     dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + data[i]
#     dp[i][2] = dp[i-1][1] + data[i]
#
# print(max(dp[n][1], dp[n][2]))


# 문제3 계단 오르기 1차원 배열로 풀기
# n = int(input())
# data = [0]
# for _ in range(n):
#     data.append(int(input()))
#
# if n == 1 :
#     print(data[1])
#     exit()
# elif n == 2:
#     print(data[1] + data[2])
#     exit()
#
# dp 테이블 정의: dp[i] 의 경우 i 지점까지 계단을 밟지 않는 최솟값, 단 i 지점은 밟지 않아야함
# dp = [0] * (n + 1)
#
# dp[1] = data[1]
# dp[2] = data[2]
# dp[3] = data[3]
#
# for i in range(3, n + 1):
#     dp[i] = data[i] + min(dp[i-2], dp[i-3])
#
# print(sum(data) - min(dp[n-1],dp[n-2]))

# 문제2 계단 오르기 문제푸는방식3
# dp 테이블 정의: n 번째 계단 까지의 최댓값, 단, n번째 계단은 꼭 밟아야함
# n = int(input())
# data = [0]
# for _ in range(n):
#     data.append(int(input()))
#
# if n == 1:
#     print(data[1])
#     exit(0)
# elif n == 2:
#     print(data[1] + data[2])
#     exit(0)
#
# dp = [0] * (n + 1)
# dp[1] = data[1]
# dp[2] = data[1] + data[2]
# dp[3] = max(data[1], data[2]) + data[3]
#
# for i in range(3, n + 1):
#     dp[i] = max(dp[i-2] + data[i], dp[i-3] + data[i-1] + data[i])
#
# print(dp[n])

# 문제4 RGB 거리
# 와!!! 한방에 풀었어 너무 짜맀하다 ㅋㅋㅋㅋㅋㅋㅋ
# dp에 적응해가고있어
# n = int(input())
# dp = [[0] * 3 for i in range(n)]
#
# data = []
# for i in range(n):
#     data.append(list(map(int, input().split())))
#
# # dp 테이블 = dp[i][j] i번째 j를 선택했을 때 모든 선택에 대한 최솟값
# dp[0][0] = data[0][0]
# dp[0][1] = data[0][1]
# dp[0][2] = data[0][2]
#
# for i in range(1, n):
#     # dp[n][0]번째를 고른경우 dp[n-1][1], dp[n-1][3]의 최솟값 만 알면 됨
#     dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + data[i][0]
#     dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + data[i][1]
#     dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + data[i][2]
#
# print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))

# 문제5 2*n 타일링
# 테이블 정의
# dp[n] => n 번째까지 타일을 채우는 모든 방법의 수
# -> 알고보니 피보나치 수열과 동일한값. 초깃값 제외
# 타일링 문제
# n = int(input())
# dp = [0] * 1001
# dp[1] = 1
# dp[2] = 2
# for i in range(3, n + 1):
#     dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
# print(dp[n])


# 문제6 구간 합 구하기4
# # 구간의 합을 미리 계산해놓는 문제 prefix sum 이라고 지칭한다
# n, m = map(int, input().split())
# data = list(map(int, input().split()))
# # dp 테이블 정의: dp[n] = 1번째 부터 n 번째까지의 합
# dp = [0] * 100001
# # 초깃값 설정
# dp[1] = data[0]
# # n번 만의 연산으로 1부터 n 까지의 구간 합을 모두 구할 수 있다
# for i in range(2, n + 1):
#     dp[i] = dp[i-1] + data[i-1]
#
# result = []
# for i in range(m):
#     s, e = map(int, input().split())
#     result.append(dp[e] - dp[s-1])
#
# for r in result:
#     print(r)

# 문제7 1로 만들기 2
# n = int(input())
# dp = [0] * (int(1e6) + 1)
# load = [0] * (int(1e6) + 1)
#
# dp[1] = 0
# load[1] = 0
#
# for i in range(2, n + 1):
#     dp[i] = dp[i - 1] + 1
#     load[i] = i - 1
#
#     if i % 2 == 0:
#         if dp[i // 2] + 1 < dp[i]:
#             dp[i] = dp[i // 2] + 1
#             load[i] = i // 2
#
#     if i % 3 == 0:
#         if dp[i // 3] + 1 < dp[i]:
#             dp[i] = dp[i // 3] + 1
#             load[i] = i // 3

# print(dp[n])
# print(n, end=" ")
# while True:
#     if n == 1:
#         break
#     print(load[n], end=" ")
#     n = load[n]


# 잘 짠 코드 list + 연산으로 해결
# N = int(input())
#
# result = [[0, []] for _ in range(N + 1)]  # [최솟값, 경로 리스트]
# result[1][0] = 0  # 최솟값
# result[1][1] = [1]  # 경로를 담을 리스트
#
# for i in range(2, N + 1):
#
#     # f(x-1) + 1
#     result[i][0] = result[i - 1][0] + 1
#     result[i][1] = result[i - 1][1] + [i]
#
#     # f(x//3) + 1
#     if i % 3 == 0 and result[i // 3][0] + 1 < result[i][0]:
#         result[i][0] = result[i // 3][0] + 1
#         result[i][1] = result[i // 3][1] + [i]
#
#     # f(x//2) + 1
#     if i % 2 == 0 and result[i // 2][0] + 1 < result[i][0]:
#         result[i][0] = result[i // 2][0] + 1
#         result[i][1] = result[i // 2][1] + [i]
#
# print(result[N][0])
# for i in result[N][1][::-1]:  # 뒤집은 뒤 출력
#     print(i, end=' ')