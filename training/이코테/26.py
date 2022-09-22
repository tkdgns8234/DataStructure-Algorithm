import heapq

N = int(input())

hq = []
for _ in range(N):
    heapq.heappush(hq, int(input()))

result = 0
while len(hq) >= 2:
    first = heapq.heappop(hq)
    second = heapq.heappop(hq)
    result += (first + second)
    heapq.heappush(hq, first + second)

print(result)
