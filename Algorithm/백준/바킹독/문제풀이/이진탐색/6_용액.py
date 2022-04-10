# 6. 용액
# 두 가지 풀이를 할 수 있다.
# 이진탐색의 bisect 를 이용한 풀이
# 투포인터를 이용한 풀이

# 1. bisect 를 이용한 풀이
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
