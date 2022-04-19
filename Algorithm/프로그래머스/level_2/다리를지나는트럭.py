# 완전탐색은 시간초과일거같았는데
# 성공했다
# 효율성 제약이 없어서그런가?
# 1억정도의 연산이 필요한데,

from collections import deque
def solution(bridge_length, weight, truck_weights):
    birdge_q = deque([0 for i in range(bridge_length)])
    truck_q = deque(truck_weights)
    now_weight = 0
    answer = 0
    while truck_q:
        w = birdge_q.popleft()
        now_weight -= w

        if weight - now_weight >= truck_q[0]:
            truck = truck_q.popleft()
            birdge_q.append(truck)
            now_weight += truck
        else:
            birdge_q.append(0)
        answer += 1
    answer += len(birdge_q)
    return answer

v = solution(100,	100,	[10,10,10,10,10,10,10,10,10,10])
print(v)

# 코드 개선
# (구조만 조금 변경)
from collections import deque

def solution(bridge_length, weight, truck_weights):
    q = deque([0 for i in range(bridge_length)])
    trucks = deque(truck_weights)

    now_weight = 0
    answer = 0
    while q:
        w = q.popleft()
        now_weight -= w

        if trucks:
            if weight - now_weight >= trucks[0]:
                truck = trucks.popleft()
                q.append(truck)
                now_weight += truck
            else:
                q.append(0)
        answer += 1
    return answer


v = solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
print(v)

