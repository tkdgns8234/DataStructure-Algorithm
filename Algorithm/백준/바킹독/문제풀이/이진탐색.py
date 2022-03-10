# 1. 숫자 카드
# 이진탐색으로 풀었으나, set 자료구조를 활용하면 더 빠르다
# import sys
# import bisect
# input = sys.stdin.readline
#
# n = int(input())
# data1 = list(map(int, input().split()))
# m = int(input())
# data2 = list(map(int, input().split()))
#
# def binary_search(arr, target):
#     left = bisect.bisect_left(arr, target)
#     right = bisect.bisect_right(arr, target)
#     return True if right - left > 0 else False
#
# data1.sort()
#
# for i in data2:
#     if binary_search(data1, i):
#         print(1, end=" ")
#     else:
#         print(0, end=" ")

# 2. 차집합
# set 자료구조 + 언패킹 이용
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# data1 = list(map(int, input().split()))
# data2 = set(map(int, input().split()))
#
# data1.sort()
# result = []
# for i in data1:
#     if i not in data2:
#         result.append(i)
#
# print(len(result))
# if len(result) > 0:
#     print(*result)

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

# 5. 멀티버스 2
# 좌표압축 문제인데 이진탐색 방법이 아닌 dictionary 를 이용해서 푸는 방법이 있다
# 이게 더 간단해보이는데 해보자
# M, N = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(M)]
#
# new_data = [[] for _ in range(M)]
# dict = {}
# for i in range(len(data)):
#     # !!!!!주의!!!!! set 사용 시, 순서가 바뀔 수 있음, 위 data 에서 set 으로 중복 제거 시 원하는 답 도출 불가
#     temp = sorted(list(set(data[i])))
#     for j in range(len(temp)):
#         dict[temp[j]] = j
#     for j in data[i]:
#         new_data[i].append(dict[j])
#
# cnt = 0
# for i in range(0, M-1):
#     for j in range(i, M):
#         if i == j:
#             continue
#         if new_data[i] == new_data[j]:
#             cnt += 1
#
# print(cnt)


# 6. 용액
# 두 가지 풀이를 할 수 있다.
# 이진탐색의 bisect_right 를 이용한 풀이
# 투포인터를 이용한 풀이

# 1. bisect_right 를 이용한 풀이
# 처음 이진탐색을 이용한 풀이를 떠올렸을 때 각 요소를 모두 이진탐색으로 찾는 N * NlogN 의 풀이밖에 떠오르지 않아 불가능하다고 생각했다.
# 생각을 바꿔 [-100, -4, 1, 2, 3, 4, 6, 7, 9] 라는 배열이 있을 때, -4 라는 값은 4를 더했을 때 0에 가장 가까운 수 이므로
# 파이썬의 bisect 라이브러리를 이용해 4에 가까운 인덱스를 찾고 그 좌, 우 인덱스까지 고려하여 특정 숫자에 대한 덧셈의 최솟값을 찾을 수 있음을 깨닳았다
# 시간복잡도 N * 3*LogN (idx-1, idx, idx+1)

# import bisect
#
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()
#
# ans1 = 1e9
# ans2 = 1e9
# for i in range(len(data)):
#     idx = bisect.bisect_left(data, -data[i]) # -data[i] 이거나 -data[i]보다 큰 수 중 가장 작은수 위치 반환
#     data[i]와 더했을 때 값이 가장 작은 원소는 data[idx+1] 혹은 data[idx] 혹은 data[idx-1]이다.
#     if idx+1 != i and idx + 1 < n and abs((ans1+ans2)) > abs(data[i]+data[idx+1]):
#         ans1 = data[i]
#         ans2 = data[idx+1]
#     if idx != i and idx < n and abs(ans1+ans2) > abs(data[i]+data[idx]):
#         ans1 = data[i]
#         ans2 = data[idx]
#     if idx-1 != i and idx > 0 and abs(ans1+ans2) > abs(data[i]+data[idx-1]):
#         ans1 = data[i]
#         ans2 = data[idx-1]
#
# print(ans1, ans2)

# 투 포인터를 활용한 풀이
# 시간복잡도: O(N)
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()
#
# left = 0
# right = len(data)-1
#
# ans1, ans2 = 1e9, 1e9
# while left < right:
#     if abs(ans1 + ans2) > abs(data[left] + data[right]):
#         ans1 = data[left]
#         ans2 = data[right]
#
#     if data[left]+data[right] < 0:
#         left += 1
#     elif data[left]+data[right] > 0:
#         right -= 1
#     else:
#         break
#
# print(ans1, ans2)

# 7. 합이 0
# 이진탐색을 활용하는 경우 시간복잡도가 (두원소선택) n^2 * logN (나머지 하나의 원소 탐색) 이므로
# 파이썬환경에서는 이진탐색을 이용한 풀이가 불가능해보인다
# 투포인터 활용
# 아래는 참고 코드
# 스스로 풀어보자



# """
#  세 팀원 코딩 실력 합 0
#  팀을 얼마나 많이 만들 수 있는지 계산
#  결과: 합이 0이 되는 3인조 만들
#  주의: 같은 값이 연속적으로 나오는 경우 처리
# """
# import sys
# from collections import Counter
#
# n = int(sys.stdin.readline())  # 학생 수
# arr = list(map(int, sys.stdin.readline().split()))  # 학생 코딩 실력
# arr.sort()
# cnt_ = Counter(arr)  # 해당 점수에 해당하는 학생 수 얻기
# result = 0
# # 학생을 한명 씩 돌린다.
# for i, a in enumerate(arr):
#     left, right = i + 1, n - 1
#     while left < right:
#         sum_ = arr[left] + arr[right] + arr[i]
#         # 1. 점수 총합이 0인 경우, 같은 값이 있는 것에 대한 처리 필요
#         if sum_ == 0:
#             #  left값과 right 갑이 같은 경우 해당 범위 저장. -4 2 2 2 2
#             if arr[left] == arr[right]:
#                 result += right - left
#             # 다른 경우 right 값에 대한 개수 합 -4 1 1 1 3 3 3
#             else:
#                 result += cnt_[arr[right]]
#             left += 1
#         # 2. 점수 총합이 0 보다 큰 경우
#         elif sum_ > 0:
#             right -= 1
#         # 3. 점수 총합이 0 보다 작은 경우
#         elif sum_ < 0:
#             left += 1
#
# print(result)