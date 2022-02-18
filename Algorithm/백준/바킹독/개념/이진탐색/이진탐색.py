# 문제1 수 찾기
# 가장 기본적인 이진탐색
# 이진탐색 전 정렬을 수행
# 파이썬의 bisect_left, right 라이브러리의 경우 데이터가 없는 경우 0 을 리턴함
# import bisect
# n = int(input())
# data = list(map(int, input().split()))
# m = int(input())
# pivot = list(map(int, input().split()))
#
# def find_num(num):
#     left = bisect.bisect_left(data, num)
#     right = bisect.bisect_right(data, num)
#     return True if right - left > 0 else False
#
# data.sort()
# for i in pivot:
#     if find_num(i):
#         print(1)
#     else:
#         print(0)

# 문제2 좌표 압축
# import copy
# n = int(input())
# data = list(map(int, input().split()))
#
# tmp = copy.deepcopy(data)
# tmp = list(set(tmp))
# tmp.sort()
#
# def binary_search(target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#
#         if tmp[mid] == target:
#             return mid
#         elif tmp[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return None
#
# for i in data:
#     print(binary_search(i, 0, len(tmp)-1), end=" ")

# 문제3 세 수의 합
# 시간복잡도 최적화 유형의 코드
# import bisect
# def find_num(arr, num):
#     left = bisect.bisect_left(arr, num)
#     right = bisect.bisect_right(arr, num)
#     return right - left
#
# n = int(input())
# data = [int(input()) for i in range(n)]
# data.sort() # 아래 for문에서 exit를 통한 최적화를 위해 추가된 코드
#
# two = []
# for i in data:
#     for j in data:
#         two += [i+j]
# two.sort()
#
# for i in range(len(data)-1, -1, -1):
#     for j in data:
#         if find_num(two, data[i] - j):
#             print(data[i])
#             exit(0)

# 문제4 랜선자르기
# 전형적인 이분탐색 + 파라메트릭 서치 문제
# 파라메트릭 서치: 최적화 문제 (최솟값, 최댓값을 찾는 문제) 를 결정문제로 바꾸어 푸는 것

# k : 이미가지고있는 랜선의 갯수 n: 필요한 랜선의 갯수
# k, n = map(int, input().split())
# data = [int(input()) for i in range(k)]
#
# start = 1
# end = max(data)
# result = 0
#
# while start <= end:
#     mid = (start + end) // 2
#
#     count = 0
#     for i in data:
#         count += i // mid
#
#     if count >= n:
#         start = mid + 1
#         result = mid
#     else:
#         end = mid - 1
#
# print(result)