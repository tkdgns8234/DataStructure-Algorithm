# 정의: 왼쪽 서브트리의 모든 값은 부모노드보다 작고 오른쪽 서브트리의 모든 노드들은 부모노드보다 큰 이진 트리
# 삽입, 삭제, 탐색 모두 O(logn) 시간만에 가능
# => 해시가 무조건 좋네? 할 수 있지만 데이터의 크기비교를할땐 이진탐색트리를 사용해야한다
# 해시는 충돌문제도 있고
# 삽입, 탐색 -> 좌우 데이터 크기를 확인하면서 탐색 및 삽입하면됨
# 삭제 ->
# 자식노드가 0 개인 경우 그냥 삭제해도 됨
# 자식노드가 1 개인 경우 삭제 후 자식노드를 삭제된 위치로
# 자식노드가 2 개인 경우 삭제된 노드보다 크면서 가장 작은노드를 해당 위치로 대입시키면 됨

# 편향트리의 경우 O(logn) 이 아니라 O(n) 이 될 수 있음
# -> 균형이진탐색트리가 존재


# 문제1 이중 우선순위 큐
# import heapq
# import sys
# input = sys.stdin.readline
# n = int(input())
#
# for _ in range(n):
#     maxq, minq = [], []
#     visited = [False] * 1_000_001 #최소힙, 최대 힙 간의 동기화를 위해 필요함 (잘 보면 데이터도 튜플형태로 넣는다 (값, id) id 를 기준으로 동기화작업을 진행)
#     test_count = int(input())
#     for i in range(test_count):
#         test = input().split()
#         if test[0] == 'I':
#             heapq.heappush(maxq, (-int(test[1]), i)) # 파이썬은 최소 힙만 지원
#             heapq.heappush(minq, (int(test[1]), i))
#             visited[i] = True
#         elif test[0] == "D":
#             if test[1] == '-1': # 최솟값을 삭제하는 연산
#                 while minq and not visited[minq[0][1]]:
#                     heapq.heappop(minq)
#                 if minq:
#                     visited[minq[0][1]] = False
#                     heapq.heappop(minq)
#             elif test[1] == "1":
#                 while maxq and not visited[maxq[0][1]]:
#                     heapq.heappop(maxq)
#                 if maxq:
#                     visited[maxq[0][1]] = False
#                     heapq.heappop(maxq)
#
#     while maxq and not visited[maxq[0][1]]:
#         heapq.heappop(maxq)
#     while minq and not visited[minq[0][1]]:
#         heapq.heappop(minq)
#     if maxq:
#         print(-maxq[0][0], minq[0][0], sep=" ")
#     else:
#         print("EMPTY")

# 문제2 보석 도둑
# 다시풀자
