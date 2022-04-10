# 4. 나무 자르기
# 이것 또한 파라메트릭 서치 문제
# import sys
# input = sys.stdin.readline
#
# def binary_search(start, end):
#     ans = 0
#     while start <= end:
#         mid = (start + end) // 2
#
#         length = 0
#         for i in data:
#             if i - mid > 0:
#                 length += i - mid
#
#         if length < M:
#             end = mid - 1
#         else:
#             start = mid + 1
#             ans = mid
#
#     return int(ans)
#
#
# N, M = map(int, input().split())
# data = list(map(int, input().split()))
#
# print(binary_search(0, 1e9))
