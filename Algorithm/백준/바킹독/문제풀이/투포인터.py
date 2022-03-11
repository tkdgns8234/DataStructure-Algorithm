# 1. 소수의 연속합
# pass

# 2. 수들의 합2
# n, m = map(int, input().split())
# data = list(map(int, input().split()))
#
# end = 0
# sum_ = 0
# count = 0
# for start in range(n):
#     while sum_ < m and end < n:
#         sum_ += data[end]
#         end += 1
#     if sum_ == m:
#         count += 1
#     sum_ -= data[start]
# print(count)

# 3. List of Unique Numbers
# [1,2,3,4,5...n] 최대 O(n^2) 보다는 작다
# 처음에 계산했을 때 위 방법이 O(n^2) 가 아닐까 해서 해당 풀이로 풀지 않고 풀이를 참조했는데,
# 이게 되네??/?
# n^2에 가까워보인다고 생각했는데
# 다시 보니 투포인터 유형 자체가 대부분 저런식으로 풀이하고있음 O(N) 에 가까운거였어
# 아래와같은 방식으로(투포인터로) 풀이했을 때 O(n^2)를 O(N) 에 가깝게 풀이할 수 있다고 기억하자

#
# n = int(input())
# data = list(map(int, input().split()))
# chk = [False] * 100_002
#
# ans = 0
# chk[data[0]] = True
# en = 0
# for start in range(n):
#     while en < n-1 and not chk[data[en+1]]:
#         en += 1
#         chk[data[en]] = True
#     ans += (en-start+1)
#     chk[data[start]] = False
#
# print(ans)
#

# 4. 가장 긴 짝수 연속한 부분 수열
# N, M = map(int, input().split())
# data = list(map(int, input().split()))
#
# pass_ = M
# end = -1
# ans = 0
#
# for start in range(N):
#     while end < N - 1:
#         if data[end + 1] % 2 == 0:
#             end += 1
#         else:
#             if pass_ > 0:
#                 end += 1
#                 pass_ -= 1
#             else:
#                 break
#     ans = max(ans, (end - start + 1) - (M-pass_))
#     if data[start] % 2 != 0:
#         pass_ += 1
#
# print(ans)

# 5. 회전 초밥
# 길이를 구하고, 중복은 x 쿠폰이 길이 안에 없으면 + 1 set 로 관리
# N 접시수 d 초밥의 가짓수 k 연속 접시 수 c 쿠폰
# N, d, k, c = map(int, input().split())
# data = [int(input()) for _ in range(N)] * 2 # 회전하는 형태로 표현하기 위해
#
# menu_cnt = dict()
# menu = set()
# end = -1
# ans = 0
# for start in range(len(data)//2):
#     while end - start < k - 1:
#         end += 1
#         menu.add(data[end])
#         menu_cnt[data[end]] = menu_cnt.get(data[end], 0) + 1
#     ans = max(ans, len(menu) + 1 if c not in menu else len(menu))
#
#     if menu_cnt[data[start]] <= 1:
#         menu.remove(data[start])
#     menu_cnt[data[start]] -= 1
#
# print(ans)

# 6. 겹치는 건 싫어
# N, K = map(int, input().split())
# data = list(map(int, input().split()))
#
# dic = dict()
#
# end = 0
# ans = 0
# for start in range(N):
#     while end < N:
#         if dic.get(data[end], 0) < K:
#             dic[data[end]] = dic.get(data[end], 0) + 1
#             end += 1
#         else:
#             break
#     ans = max(ans, end - start)
#     dic[data[start]] = dic.get(data[start], 0) - 1
#
# print(ans)
