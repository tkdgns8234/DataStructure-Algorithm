# 이미 푼 문제, 다시풀자
from collections import deque

def solution(priorities, location):
    q = deque([(i, priorities[i]) for i in range(len(priorities))])

    order = 0
    while q:
        idx, priority = q.popleft()
        if q and max([i[1] for i in q]) > priority:
            q.append((idx, priority))
        else:
            order += 1
            if idx == location:
                return order

v = solution([2, 1, 3, 2],	2)
print(v)