# 1. 소수의 연속합
# 일단 소수를 구해야하는데
# 2 또는 3으로 나누어 떨어지지 않으면 소수
# import math
# import sys
#
# input = sys.stdin.readline
#
# N = int(input().rstrip())
#
#
# def prime_numbers(n):
#     prime_numbers = [i for i in range(n + 1)]
#     primenumbers = []
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if prime_numbers[i] == 0:
#             continue
#         j = 2
#         while i * j <= n:
#             prime_numbers[i * j] = 0
#             j += 1
#
#     for i in prime_numbers[2:]:
#         if i != 0:
#             primenumbers.append(i)
#     return primenumbers
#
#
# primeArr = prime_numbers(N)
# count = 0
# left = 0
# intervalSum = 0
#
# for right in range(len(primeArr)):
#     intervalSum += primeArr[right]
#
#     while intervalSum > N:
#         intervalSum -= primeArr[left]
#         left += 1
#
#     if intervalSum == N:
#         count += 1
#
# print(count)
N = int(input())
array = [False, False] + [True] * (N-1)
data = []

for i in range(2, N+1):
    if array[i]:
        data.append(i)
    for j in range(i*2, N+1, i):
        array[j] = False

ans = 0
left, right = 0, 0
sum_ = 0

while True:
    if sum_ >= N:
        if sum_ == N:
            ans += 1
        sum_ -= data[left]
        left += 1
    elif right == len(data):
        break
    else:
        sum_ += data[right]
        right += 1
print(ans)
