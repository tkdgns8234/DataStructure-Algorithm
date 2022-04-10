# 문제6 휴게소 세우기
# ---------------------------------- 전혀 틀린 풀이.. greedy는 절대 성립이 안됨
# 이진 탐색으로 풀어야함
# 이진탐색으로 다시풀자

# def find_max_dist():
#     global rest_store
#     rest_store.sort()
#     length = len(rest_store)
#
#     #초깃값 설정
#     position1 = rest_store[0]
#     position2 = rest_store[1]
#     max_val = position2 - position1
#
#     for i in range(length - 1):
#         if max_val < rest_store[i + 1] - rest_store[i]:
#             max_val = rest_store[i + 1] - rest_store[i]
#             position1 = rest_store[i]
#             position2 = rest_store[i + 1]
#
#     # 마지막 rest store와 고속도로간의 거리 차이도 계산
#     if max_val < distance - rest_store[length-1]:
#         max_val = distance - rest_store[length-1]
#         position1 = rest_store[length-1]
#         position2 = distance
#
#     return max_val, position1, position2
#
#
# n, m, distance = map(int, input().split())
# rest_store = list(map(int, input().split()))
# added_dist = []
#
# for i in range(m):
#     max_val, store1, store2 = find_max_dist()
#
#     if (store1 + store2) % 2 > 0:
#         exist = False
#         val = 1
#         for s in added_dist:
#             if s[0] <= store1 and store2 >= s[1]:
#                 exist = True
#                 if s[2] == 1:
#                     val = -1
#                     s[2] = -1
#                 elif s[2] == -1:
#                     val = 1
#                     s[2] = 1
#
#         if not exist:
#             added_dist.append([store1, store2, 1])
#         rest_store.append((store1 + store2) // 2 + val)
#     else:
#         rest_store.append((store1 + store2) // 2)
#
# print(find_max_dist()[0])
#
# ---------------------------------- 전혀 틀린 풀이.. greedy는 절대 성립이 안됨