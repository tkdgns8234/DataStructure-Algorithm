# 컨셉
# 보트 최대 인원 수:2
# 가장 무게가 작은 사람부터
# 이진탐색으로 같이 탈 수 있는 사람 중 가장 큰 사람을 찾고 같이 간다
# 정확도 성공 효율성 역시 실패
# 어떻게 극복하지?
# 투포인터로 풀어보자

# import bisect
# def bisect_left(start, end, visited, arr, target):
#     ret = -1
#     while start <= end:
#         mid = (start + end)//2
#
#         if arr[mid] <= target and not visited[mid]:
#             ret = mid
#             start = mid + 1
#         else:
#             end = mid - 1
#     return ret
#
# def solution(people, limit):
#     visited = [False] * len(people)
#     people.sort()
#
#     answer = 0
#     for idx, p in enumerate(people):
#         if visited[idx]: continue
#         visited[idx] = True
#         target = limit - people[idx]
#         target_idx = bisect_left(idx+1, len(people)-1, visited, people, target)
#
#         if target_idx != -1:
#             visited[target_idx] = True
#         answer += 1
#     return answer
#
# v = solution([50,70,80,50],100)
# print(v)

# 투포인터 활용
# 성공!!!!!!!!!!!!!!!!!!!!!!!!!!!
def solution(people, limit):
    people.sort()
    left, right = 0, len(people)-1

    answer = 0
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        answer += 1

    return answer


# 다른 풀이
# deque를 활용한 풀이 (투포인터 방식과 동일함)
from collections import deque

def solution(people, limit):
    result = 0
    deque_people = deque(sorted(people))

    while deque_people:
        left = deque_people.popleft()
        if not deque_people:
            return result + 1
        right = deque_people.pop()
        if left + right > limit:
            deque_people.appendleft(left)
        result += 1
    return result

