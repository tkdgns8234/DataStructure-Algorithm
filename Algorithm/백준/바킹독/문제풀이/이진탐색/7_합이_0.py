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
