# 9. 공유기 설치
# 파라메트릭 서치문제, 이코테에서 풀어봤던 문제로 기억한다
# 원하고자하는 답 (두 공유기 사이의 최대거리) 를 매개변수로 넣고
# C개 이상 설치할 수 있는지 확인한다
# import sys
# input = sys.stdin.readline
# def binary_search(start, end):
#     ans = 0
#     while start <= end:
#         mid = (start+end)//2
#
#         # mid 로 길이 설정하는 경우 몇개의 공유기 설치할 수 있는지 확인
#         count = 1
#         val = data[0]
#         for i in range(1, N):
#             if data[i] >= val + mid:
#                 val = data[i]
#                 count += 1
#
#         # count = 1
#         # s = 0
#         # flag = True
#         # while flag:
#         #     flag = False
#         #     for i in range(s + 1, N):
#         #         if data[i] - data[s] >= mid:
#         #             count += 1
#         #             s = i
#         #             flag = True
#         #             break
#
#         if count < C:
#             end = mid - 1
#         else:
#             start = mid + 1
#             ans = mid
#     return ans
#
#
# N, C = map(int, input().split())
# data = list(int(input().rstrip()) for _ in range(N))
# data.sort()
#
# max_len = data[N-1] - data[0]
# print(binary_search(0, max_len))
