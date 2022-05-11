# 1~ 10000일동안 하루씩 n일에 할수있는 강의 중 가치가 가장 높은것
# 실패

# import heapq
# import sys
# input = sys.stdin.readline
#
# N = int(input())
# request = []
# for _ in range(N):
#     p,d = map(int, input().split())
#     request.append([d, p])
# heapq.heapify(request)
#
# ans = 0
# day = 1
# while request:
#     candidate = []
#     while request and day >= request[0][0]:
#         heapq.heappush(candidate, -request[0][1])
#         heapq.heappop(request)
#     if candidate:
#         v = -heapq.heappop(candidate)
#         ans += v
#     day += 1
# print(ans)


# 매 day마다 가장 가치있는걸 하는것만이 정답이 아님
# 반례가 있음
# (1, 1), (10, 2), (10, 2) 인 경우 최댓값은?? 20이다
# 매 day마다 가장 가치있는걸 추가하되
# day보다 초과된경우 대입하고 최솟값 pop
# 나중에 다시풀자

import heapq
import sys
input = sys.stdin.readline

N = int(input())
request = [list(map(int, input().split())) for _ in range(N)]
request.sort(key=lambda x:x[1])

candidate = []
for p, d in request:
    heapq.heappush(candidate, p)
    if len(candidate) > d:
        heapq.heappop(candidate)
print(sum(candidate))