# 1. 소수의 판별 (x^1/2) (루트)
# 1-2. 에라토스테네스의 체 (Nloglogn)
# 2. 투 포인터
# 2-1. 특정 합을 가지는 부분 연속 수열 찾기 (시작점을 오른쪽으로 이동 = 항상감소, 끝점 오른쪽이동: 항상 감소 하기 때문에 투포인터 사용 가능)
# 2-2. 정렬된 두 원소의 합집합 (병합정렬과 동일한 원리)
# 3. 구간 합 계산O(N+M) N개의 데이터과 M 개의 쿼리

# 1. 소수의 판별
# 약수의 법칙을 확인 해 보면 판별 하고자 하는 숫자의 제곱근 범위까지만 확인 하면 된다
# 소수 구하기
# import math
# def is_prime_number(n):
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# N = int(input())
# print(is_prime_number(N))

# 1-2. 에라토스테네스의 체
# 특정 구간의 소수 구하기
# import math
# def get_prime_number(n):
#     result = [True] * (n + 1)
#
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if result[i]:
#             for j in range(i*2, n+1, i):
#                 result[j] = False
#
#     ans = []
#     for i in range(2, n+1):
#         if result[i]:
#             ans.append(i)
#     return ans
#
# N = int(input())
# print(get_prime_number(N))

# 2-1. 특정 합을 가지는 부분 연속 수열 찾기
# data = [1,2,3,2,5]
# n = 5 # 길이
# m = 5 # 원하는 합
#
# start, end, sum_ = 0, 0, 0
# count = 0
# # start 증가
# for start in range(n):
#     # end 가능한 만큼 이동
#     while end < n and sum_ < m:
#         sum_ += data[end]
#         end += 1
#
#     if sum_ == m:
#         count += 1
#     sum_ -= data[start]
#
# print(count)

# 2-2. 정렬된 두 원소의 합집합 (병합정렬과 동일한 원리)
# data1 = [1,4,7,9,15,16,18,22]
# data2 = [2,4,8,11,13,17,23]
# n, m = len(data1), len(data2)
#
# result = []
# p1, p2 = 0, 0
#
# while p1 < n or p2 < m:
#     if p1 >= n or (p2 < m and data1[p1] > data2[p2]):
#         result.append(data2[p2])
#         p2 += 1
#     else:
#         result.append(data1[p1])
#         p1 += 1
#
# print(result)

# 3. 구간 합 계산 (prefix_sum)
# data = [10, 20, 30, 40, 50]
#
# ps = [0]
# sum_ = 0
# for i in range(len(data)):
#     sum_ += data[i]
#     ps.append(sum_)
#
# n, m = map(int, input().split())
# print(ps[m] - ps[n-1])