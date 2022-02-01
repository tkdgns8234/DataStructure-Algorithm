# -*- coding: utf-8 -*-
# Q01 모험가길드

# n = int(input())
# sc_num = list(map(int, input().split()))
#
# sc_num.sort()
# now = 0
#
# result = 0
# while now < len(sc_num):
#     if now + sc_num[now] < len(sc_num):
#         now += sc_num[now]
#         result += 1
#     else:
#         break
#
# print(result)

# Q02 곱하기 혹은 더하기
# s = input()
#
# result = 0
#
# for i in s:
#     i = int(i)
#     if i <= 1 or result <= 1:
#         result += i
#     else:
#         result *= i
#
# print(result)

# Q03 문자열 뒤집기
# s = input()
# s = map(int, s)
#
# count_0 = 0
# count_1 = 0
#
# now = -1
# for i in s:
#     if i != now:
#         if i == 0:
#             count_0 += 1
#             now = 0
#         else:
#             count_1 += 1
#             now = 1
#
# print(min(count_0, count_1))

# Q04 만들 수 없는 금액
# 이 문제는 동전의 합을 더해나가면서 동전의 합 보다 인덱스의 값이 크면 못만드는 특징이 존재한다
# result 초깃값이 1인 이유는 동전의 합 + 1 을 만들수 있는지 없는지 다음인덱스에서 판단하려고
# 동전의 합 까진 만들수 있다 모든경우에대해

# n = int(input())
# coins = list(map(int, input().split()))
# coins.sort()
#
# result = 1
# for coin in coins:
#     if result >= coin:
#         result += coin
#     else:
#         print(result)
#         break

# Q05 볼링공 고르기
# n, m = map(int, input().split())
# l = list(map(int, input().split()))
#
# all_case = 0
# for i in range(n-1, 0, -1):
#     all_case += i
#
# c = 0
# for i in range(1, m+1):
#     if l.count(i) > 1:
#         c += (l.count(i)-1)
#
# print(all_case-c)

# Q06 무지의 먹방 라이브
# def solution(food_times, k):
#     answer = 0
#     return answer