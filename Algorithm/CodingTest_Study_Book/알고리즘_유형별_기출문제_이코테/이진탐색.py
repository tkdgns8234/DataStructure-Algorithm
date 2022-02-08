# Q27 정렬된 배열에서 특정 수의 개수 구하기
# import bisect
#
# n, target = map(int, input().split())
#
# data = list(map(int, input().split()))
#
# left = bisect.bisect_left(data, target)
# right = bisect.bisect_right(data, target)
# result = right - left
# result = -1 if result == 0 else result
# print(result)

# Q28 고정점 찾기
# def binary_search(arr, start, end):
#     while start <= end:
#         mid = (start+end) // 2
#         if arr[mid] == mid:
#             return mid
#         if arr[mid] < mid:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return None
#
#
# n = int(input())
# data = list(map(int, input().split()))
#
# val = binary_search(data, 0, len(data) - 1)
# print(val if val is not None else -1)

# Q29 공유기 설치
# 아래 코드에서 실패 어떻게 해결할지 정확하게 정하고 문제풀자

# house_loc = []
# wifi_loc = []
#
# n, wifi_num = map(int, input().split())
# for i in n:
#     house_loc.append(int(input()))
#
# house_loc.sort()
#
# def find_largest_start_stop(wifi_loc):
#     dis = -1
#
#     for i in range(len(wifi_loc)-1):
#         if dis < wifi_loc[i + 1] - wifi_loc[i]:
#             dis = wifi_loc[i + 1] - wifi_loc[i]
#             start = wifi_loc[i]
#             end = wifi_loc[i + 1]
#
#     return start, end
#
#
# def build_wifi():
#     if wifi_num == 2:
#         house_loc[len(house_loc) - 1] - house_loc[0]
#
#     # 시작과 끝 지점 삽입
#     wifi_loc.append(house_loc[0])
#     wifi_loc.append(len(house_loc) - 1)
#

# Q29 공유기 설치
# 전형적인 파나메트릭 서치 문제이다
# n, c = map(int, input().split())
# house_location = [int(input()) for i in range(n)]
# house_location.sort()
#
# result = 0
# start = 1 # 최소간격
# end = house_location[-1] - house_location[0] # 최대 간격
#
# while start <= end:
#     mid = (start+end) // 2
#     wifi_cnt = 1
#     loc = house_location[0]
#
#     for i in range(1, len(house_location)):
#         if house_location[i] >= loc + mid:
#             wifi_cnt += 1
#             loc = house_location[i]
#
#     if wifi_cnt >= 3:
#         start = mid + 1
#         result = mid
#     else:
#         end = mid - 1
#
# print(result)

# Q30 가사 검색
# 다시 풀자
def solution(words, queries):
    answer = []
    return answer