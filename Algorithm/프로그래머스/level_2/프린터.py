from collections import deque
def solution(priorities, location):
    priorities = [(p, i) for i, p in enumerate(priorities)] #우선순위, 인덱스
    q = deque(priorities)
    count = 0
    while q:
        now = q.popleft()
        flag = False
        for i in range(len(q)):
            if now[0] < q[i][0]:
                flag = True
                break
        if flag:
            q.append(now)
        else:
            count += 1
            if now[1] == location:
                return count
solution([2, 1, 3, 2], 2)

# 더 좋은 풀이
# any 사용
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer