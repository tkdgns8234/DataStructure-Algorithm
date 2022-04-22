# 시간복잡도 안될 줄 알았는데 통과했네
# 여러모로 TC도 부족하고 미완성문제인거같다
# 일단 pass

import heapq

def solution(operations):
    pq = []
    for operation in operations:
        op, num = operation.split()
        if op == 'I':
            heapq.heappush(pq, int(num))
        else:
            if not pq:
                continue
            if int(num) == -1:
                heapq.heappop(pq)
            else:
                pq = [-i for i in pq]
                heapq.heapify(pq)
                heapq.heappop(pq)
                pq = [-i for i in pq]
                heapq.heapify(pq)
    answer = [0, 0]
    if pq:
        answer[1] = heapq.heappop(pq)
        if pq:
            pq = [-i for i in pq]
            heapq.heapify(pq)
            answer[0] = -heapq.heappop(pq)
    return answer

v = solution(["I 3", "I 2", "I 1", "D 1", "D 1", "I 3", "D -1"])
print(v)