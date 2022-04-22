import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while scoville:
        now = heapq.heappop(scoville)
        if now >= K:
            return answer
        if scoville:
            next = heapq.heappop(scoville)
            heapq.heappush(scoville, next*2+now)
        answer += 1
    return -1

v = solution([1, 2, 3, 9, 10, 12]	,7)
print(v)