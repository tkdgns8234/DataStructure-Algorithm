# 문제 4. 트럭
# 최대 10만의 시간 소요: 시간복잡도 충분
# 지문 자체를 이해하는데 오래걸렸어;;
from collections import deque
# 트럭수, 다리길이, 다리 최대 하중
n, bride_l, birdge_w = map(int, input().split())
truck = list(map(int, input().split()))

second = 0 # 소요 시간
truck_w = 0 # 총 트럭 무게
index = 1 # 몇 번째 트럭이 들어갈 차례인지

q = deque()
q.append((truck[0], 0 + bride_l))  # (무게, 종료시간)
truck_w += truck[0]
while q:
    second += 1

    if q[0][1] == second:
        temp = q.popleft()
        truck_w -= temp[0]

    if index < n and (birdge_w - (truck_w + truck[index])) >= 0:
        q.append((truck[index], second + bride_l))
        truck_w += truck[index]
        index += 1

print(second + 1)

# 문제4. 트럭
# 보기에 좀 더 간단해보이고 좋은코드를 찾았다
# bridge 를 실제로 만들고 트럭을 붙이는 형식

# import sys
# from _collections import deque
# input = sys.stdin.readline
#
# N, W, L = map(int, input().split())
# trucks = deque(list(map(int, input().split())))
#
# answer = 0
# bridge = deque([0 for _ in range(W)])
#
# while trucks:
#     bridge.popleft()
#     if sum(bridge) + trucks[0] <= L:
#         truck = trucks.popleft()
#         bridge.append(truck)
#     else:
#         bridge.append(0)
#     answer += 1
# answer += W
# print(answer)
