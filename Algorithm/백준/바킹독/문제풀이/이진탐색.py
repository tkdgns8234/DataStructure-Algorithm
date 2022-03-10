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
# 투포인터 활용 시간복잡도: O^2
# 아래는 참고 코드
# 스스로 풀어보자
# counter 사용하지 않고 반복 시 마다 data.count 를 수행하면 시간초과
# import sys
# from collections import Counter
#
# input = sys.stdin.readline
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()
# cnt_ = Counter(data)
# ans = 0
#
# for i, d in enumerate(data):
#     left = i + 1
#     right = n-1
#     while left < right:
#         sum = data[i] + data[left] + data[right]
#         # 0 인경우
#         if sum == 0:
#             # left, right 데이터가 같은 경우 중복되는 데이터만큼 +
#             # ex) -6 3 3 3 3 3 3
#             if data[left] == data[right]:
#                 ans += right-left
#             # 다른경우 right 갯수만큼 +
#             # ex) -4 1 1 1 3 3 3
#             else:
#                 ans += cnt_[data[right]]
#             left += 1
#         # 0보다 작은 경우
#         elif sum < 0:
#             left += 1
#         # 0보다 큰 경우
#         else:
#             right -= 1
# print(ans)

# 8. 세 용액
# 투포인터, 이진탐색 둘 다 가능해보이는데
# 이진탐색: 특정 수를 기준으로 두고 반복 -> 시간초과
# 투포인터로 진행
# 위 문제와 매우 유사해보인다
# import sys
# input = sys.stdin.readline
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()
#
# ans1, ans2, ans3 = 1e9, 1e9, 1e9
#
# for i in range(len(data)):
#     left, right = i + 1, len(data) - 1
#     while left < right:
#         sum_ = data[i] + data[left] + data[right]
#         if abs(sum_) < abs(ans1 + ans2 + ans3):
#             ans1, ans2, ans3 = data[i], data[left], data[right]
#
#         if sum_ == 0:
#             break
#         elif sum_ < 0:
#             left += 1
#         elif sum_ > 0:
#             right -= 1
# print(ans1, ans2, ans3)

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

# 합이 0인 네 정수
# ab, cd 합 모든경우 두개 다 구해서 이진탐색으로 찾는경우 n^2 * logn 인데, 시간 초과 느낌인데
# 투포인터도 n^3 풀이밖에 안보이네
# 두 개의 리스트로 나눈 후 dict 이용해 풀어야하는듯
# 시간복잡도: O(n^2)
# import sys
# input = sys.stdin.readline
# N = int(input())
# d1, d2, d3, d4 = [], [], [], []
#
# for _ in range(N):
#     data = list(map(int, input().split()))
#     d1.append(data[0]), d2.append(data[1]), d3.append(data[2]), d4.append(data[3])
#
# ab_dict = {}
# for i in d1:
#     for j in d2:
#         ab_dict[i+j] = ab_dict.get(i+j, 0) + 1
#
# ans = 0
# for i in d3:
#     for j in d4:
#             ans += ab_dict.get(-(i+j), 0)
#
# print(ans)