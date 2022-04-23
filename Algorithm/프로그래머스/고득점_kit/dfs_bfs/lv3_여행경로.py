# 틀린 풀이
# 문제 설명이 애매해서,, 꼭 알파벳순으로 방문하는게 아니다.
# 모든곳을 방문할 수 없으면 그 노드는 가면 안된다.
# 다시풀자

# from collections import defaultdict
#
# def solution(tickets):
#     dic = defaultdict(list)
#
#     for ticket in tickets:
#         start, end = ticket[0], ticket[1]
#         dic[start].append(end)
#
#     for i in dic:
#         dic[i].sort(reverse=True)
#
#
#     answer = ['ICN']
#     start = 'ICN'
#     while True:
#         if len(dic[start]) == 0:
#             break
#         next_start = dic[start].pop()
#         answer.append(next_start)
#         start = next_start
#     return answer
#
# v = solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
# print(v)


# 다시 풀기
# 실패. 백트래킹형식으로 잘 풀었다고생각했는데 실패했다. 효율성도 아니고 정확도에서.
import copy
from collections import defaultdict, deque

# def solution(tickets):
#     test = deque()
#     dic = defaultdict(deque)
#
#     for ticket in tickets:
#         start, end = ticket[0], ticket[1]
#         dic[start].append(end)
#
#     for i in dic:
#         dic[i] = deque(sorted(dic[i]))
#
#     answer = []
#     def btk(start, depth, arr):
#         if len(arr) == len(tickets)+1:
#             nonlocal answer
#             answer = copy.deepcopy(arr)
#
#         n_list = copy.deepcopy(dic[start])
#         for next in n_list:
#             dic[start].popleft()
#             arr.append(next)
#             btk(next, depth+1, arr)
#             arr.pop()
#             dic[start].appendleft(next)
#
#     btk('ICN', 0, ['ICN'])
#     return answer
#
# v = solution([['ICN','A'], ['A', 'C'],['A','B'],['B','D'],['C','A']])
# print(v)


# 다시
# 통과
# TC를 하나 찾아서 문제점을 찾은 후에 해결했다..
# TC (반례)경로: https://kyoung-jnn.tistory.com/entry/프로그래머스파이썬Python-여행경로-DFS-스택
# 여전히 더 좋은 방법은 있다 다른사람의 코드 아래 참조
# 위 코드에비해 개선된 점
# 1.             if not answer:
#                 answer = copy.deepcopy(arr)
# 백트래킹 형식이기 때문에 첫번쨰 정답만 처리 (정렬 순)

# 2.            dic[start].remove(next)
# pop left 하면 for문에서 도는 원소와 맞지 않는다

# import copy
# from collections import defaultdict, deque
#
# def solution(tickets):
#     test = deque()
#     dic = defaultdict(deque)
#
#     for ticket in tickets:
#         start, end = ticket[0], ticket[1]
#         dic[start].append(end)
#
#     for i in dic:
#         dic[i] = deque(sorted(dic[i]))
#
#     answer = []
#     def btk(start, depth, arr):
#         if len(arr) == len(tickets)+1:
#             nonlocal answer
#             if not answer:
#                 answer = copy.deepcopy(arr)
#
#         n_list = copy.deepcopy(dic[start])
#         for next in n_list:
#             dic[start].remove(next)
#             arr.append(next)
#             btk(next, depth+1, arr)
#             arr.pop()
#             dic[start].appendleft(next)
#
#     btk('ICN', 0, ['ICN'])
#     return answer
#
# v = solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])
# print(v)


# 다른 사람의 풀이
# https://kyoung-jnn.tistory.com/entry/프로그래머스파이썬Python-여행경로-DFS-스택
# 일반적인 dfs형태가 아니라
# stack을 활용한 dfs
# 코드가 좀 어렵다
# pop을 하고 answer 에 바로 대입해도 정답이 되는 이유는
# 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다. <-라는 조건이 있기 때문으로 보인다.
# stack을 활용한 방법도 있다는걸 인지하고 넘어가자
from collections import defaultdict

def solution(tickets):
    answer = []
    routes = defaultdict(list)

    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])

    for key in routes.keys():
        routes[key].sort(reverse=True)

    stack = ['ICN']
    while stack:
        tmp = stack[-1]

        if not routes[tmp]:
            answer.append(stack.pop())
        else:
            stack.append(routes[tmp].pop())
    answer.reverse()

    return answer

v = solution([['ICN','A'], ['A', 'C'],['A','B'],['B','D'],['C','A']])
print(v)