# 보석을 가치순으로 내림차순 정렬
# 모든 보석을 기준으로 탐색을 진행하되
# 가방은 이분탐색 보석의 무게보다 큰 값중 가장 작은 값
# bisect_left() 사용
# 실패
# 로직은 맞은거같은데 이미 사용한 가방을 어떻게 처리해야할지모르겠어 visit처리부분이 틀린거같다;

# def find_backpack(start, end, target):
#     pos = -1
#     while start <= end:
#         mid = (start+end)//2
#
#         if backpack[mid] < target:
#             start = mid + 1
#         else:
#             if visited[mid] and mid == 0:
#                 start = mid + 1
#                 continue
#             end = mid - 1
#             if not visited[mid]:
#                 pos = mid
#     return pos
#
# N, K = map(int, input().split())
# visited = [False]*K
# jewelry = []
# backpack = []
# for _ in range(N):
#     jewelry.append(list(map(int, input().split())))
# for _ in range(K):
#     backpack.append(int(input()))
#
# jewelry.sort(key=lambda x:x[1], reverse=True)
# backpack.sort()
#
# ans = 0
# for w, v in jewelry:
#     pos = find_backpack(0, K-1, w)
#     if pos != -1:
#         visited[pos] = True
#         ans += v
# print(ans)

# 힙 자료구조로 풀어야하는문제였다..
# 일단 이진탐색 코드는 아래 코드가 좀 더 적절해보이지만 시간초과 발생 코드

# from sys import stdin
# from bisect import bisect_left
#
#
# n, k = map(int, stdin.readline().split())
#
# jewels = []
# for _ in range(n):
#     jewels.append([int(x) for x in stdin.readline().split()])
#
# # 무게를 기준으로 오름차순 정렬
# jewels.sort(key=lambda x: x[0])
# # 가격을 기준으로 내림차순 정렬
# jewels.sort(key=lambda x: x[1], reverse=True)
#
# weights = []
# for _ in range(k):
#     weights.append(int(stdin.readline()))
#
# weights.sort()
#
#
# visited = [False] * (k + 1)
#
# total, i = 0, 0
#
# for jw in jewels:
#     current = bisect_left(weights, jw[0])
#     while visited[current]:
#         current += 1
#     if current < k:
#         total += jw[1]
#         visited[current] = True
#
# print(total)


# 힙을 이용해 다시 풀자
# 이진탐색일 때: 담으려는보석의 무게보다 큰 가방 중 가장 작은 가방을 찾는것을 목표료 했다.

# 그리디적으로 생각했을 때
# 크기가 가장 작은 가방부터 가방에 들어갈 수 있는 보석 중 가장 가치있는 보석을 찾는것
# 1. 가방, 보석을 무게 기준 오름차순으로 정렬하고, 가장 작은 가방부터 현재 담을 수있는 보석을 찾고
# 2. 그 보석 중 가장 큰 값을 찾는것을 반복
# 2번은 힙을 이용해 log n으로 쉽게 찾을 수 있다.
# 1번은 쥬얼리 배열에서 매번 찾는경우 O(N)*30만이므로 시간 초과 발생
# -> 쥬얼리 힙으로 구현해서 하나씩 빼낸다

# 2중 힙을 이용해야하는 문제다..
# 익숙하지 않으니 이번 기회에 heap에 좀 더 익숙해지자
import heapq
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
jewelry = []
backpack = []
for _ in range(N):
    jewelry.append(list(map(int, input().split())))
for _ in range(K):
    backpack.append(int(input()))

heapq.heapify(jewelry)
# jewelry.sort(key=lambda x:x[0], reverse=True)
backpack.sort()

ans = 0
candidate = []
for backpack_w in backpack:
    while jewelry and backpack_w >= jewelry[0][0]:
        heapq.heappush(candidate, -jewelry[0][1]) #max heap
        heapq.heappop(jewelry)
    if candidate:
        ans -= heapq.heappop(candidate)
print(ans)