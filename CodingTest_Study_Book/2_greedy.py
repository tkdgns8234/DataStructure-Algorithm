# 그리디 알고리즘 (탐욕법)
# 현재 상황에서 지금 당장 좋은것만 고르는 방법
# 대표적인 예로 거스름돈 문제가 존재함 (거슬러 줘야할 동전의 최소 갯수)

# 거스름돈 문제
# 거슬러 줄 때 최소 동전의 수 구하는 문제
# 시간복잡도: 화폐의 종류(cost_list)가 K라고 가정할 때  O(K)
# 화폐의 큰 단위가 작은 단위 의 항상 배수이기 때문에 그리디 알고리즘으로 해결할 수 있었다 //그리디의 경우 이처럼 조건이 중요함
# ex 화폐단위가 500,400,100 인 경우
# 800 원을 거슬러줄 때 500원,100원*3 이 아닌, 400원*2 가 더 적은 수의 동전을 거슬러 준다.

# n = 1260
# sum = 0
# cost_list = [500, 100, 50, 10]
#
# for cost in cost_list:
#     sum += n//cost
#     n %= cost
#
# print("최소 동전의 갯수: %d" % sum)


# 실전 문제
# #1 큰 수의 법칙 (limit 30M)
# import sys
#
# N, M, K = map(int, sys.stdin.readline().rstrip().split())
# L = list(map(int, input().split()))
#
# max1 = -1
# max2 = -1
#
# for i in L:
#     if max1 == -1:
#         max1 = i
#         continue
#
#     if i > max1:
#         max1 = i
#     elif i > max2:
#         max2 = i
#
#
# m = M//K
# n = m*K
#
# print(max1*n + (M-n)*max2)
# -> 정확하게 틀렸다
# 1. 파이썬에서는 sort 라는 내장 함수를 지원 한다 (오름차순 정렬)
# 2. 최댓값, 그다음 최댓값이 몇 번인지도 틀렸다
# --> 항상 문제를 풀 때 때려, 끼워 맞추기 식으로 해결 하려 하지 말고
# 처음에 문제를 살펴 보고, 어떤 !!식!!으로 해결 할지 정하고 코드를 작성 하자

# 다시 풀자
# 큰 수의 법칙
# import sys
#
# N, M, K = map(int, sys.stdin.readline().rstrip().split())
# L = list(map(int, input().split()))
#
# L.sort()
# max1 = L[N-1]
# max2 = L[N-2]
#
# max1_count = int(M / (K+1)) * K + M % (K+1)
# max2_count = M - max1_count
#
# print(max1 * max1_count + max2 * max2_count)
# 논리적으로 수식을 만드는것처럼

# 실전 문제
# #2숫자 카드 게임 (limit 30M)
# 매우 쉬워보이는데?
#
# # n 행 m 열
# n, m = map(int, input().split())
# # 최솟값
# min_max = -1
#
# # 배열 만들기 (0으로 초기화)
# num_list = [[0 for _ in range(m)] for _ in range(n)]
#
# # input 받기
# for i in range(n):
#      num_list[i] = list(map(int, input().split()))
#
# for i in range(n):
#     num_list[i].sort()
#
# for i in range(n):
#     if num_list[i][0] > min_max:
#         min_max = num_list[i][0]
#
# print(min_max)
# -> 맞았지만 시간 복잡도가 너무 크다 sort() 명령어의 경우 O(logn) 이 아니라 nLogn 만큼 소요된다
# -> O(n제곱) 만큼의 시간이 소요된다
# -> python의 min, max 함수를 사용하면 좀 더 빠르게 처리할 수 있다.


# 실전 문제
# #3 1이 될 때 까지
# 이것도 매우 쉬워 보이는데?
# n, k = map(int, input().split())
# count = 0
# while True:
#     if n == 1:
#         break
#     if n%k == 0:
#         n /= k
#     else:
#         n -= 1
#     count += 1
# print(count)
# print(n)
# 이 식에도 꼭 필요한 조건이 있다.  k 가 2이상의 숫자여야만 하는 것. 1인 경우 계속 1로 나누게 된다.
# n과 k 숫자의 제한이 1억이 넘어가는 경우 매우 느려질 수 있다
# 따라서 -1을 효율적으로 하도록 코드를 다시 작성해보자

# n, k = map(int, input().split())
# count = 0
# target = 0
# while True:
#     if n < k:
#         break
#     if n % k != 0:
#         target = (n // k * k)
#         count += (n - target)
#         n = target
#     else:
#         n /= k
#     count += 1
# count += (n-1)
#
# print(count)
# print(n)
# if문 제거 하고도 할 수 있다 이러면 상수 시간 이지만 시간복잡도가 더 줄어들겠네

