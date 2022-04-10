# 3. 과자 나눠 주기
# 파라메트릭 서치문제같은데
# 시간복잡도가 안될거같은데,, 일단 해볼까 예측시간복잡도: log10억 * 과자 수 -> 2억5천
# 최적화를 넣으면 되려나
# import sys
# input = sys.stdin.readline
#
# def binary_search(start, end):
#     ans = 0
#     while start <= end:
#         mid = (start+end)//2
#
#         count = 0
#         for i in data:
#             if i // mid < 0:
#                 break
#             count += i//mid
#
#         if M > count:
#             end = mid - 1
#         else:
#             start = mid + 1
#             ans = mid
#     return int(ans)
#
#
# M, N = map(int, input().split())
# data = list(map(int, input().split()))
# data.sort(reverse=True)
#
# print(binary_search(1, data[0]))
