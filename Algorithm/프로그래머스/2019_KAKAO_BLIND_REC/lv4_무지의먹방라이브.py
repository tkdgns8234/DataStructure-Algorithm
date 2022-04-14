import heapq

def solution(food_times, k):
    q = []
    if sum(food_times) <= k:
        return -1
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    total_time = 0
    prev_time = 0

    while q:
        now = q[0][0]
        time = (now - prev_time) * len(q)

        if total_time + time < k:
            total_time += time
            heapq.heappop(q)
            prev_time = now
        else:
            break

    index = (k - total_time) % len(q)
    q.sort(key=lambda arr: arr[1])
    answer = q[index][1]
    return answer

v = solution([1,2,3], 7)
print(v)



# 재풀이 실패
# ㄷ ㅏ 했는데, index 계산을 못해먹겠어;
import collections

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    for i in range(len(food_times)):
        food_times[i] = [i+1, food_times[i]]  #idx, num

    food_times.sort(key=lambda x: x[1]) # 음식 갯수 기준 정렬

    q = collections.deque(food_times)

    prev = 0
    while q:
        temp = q.popleft()[1]
        now = temp - prev
        prev = temp

        eat_cnt = now * (len(q)+1)
        if eat_cnt < k:
            k -= eat_cnt
        else:
            pos = k % len(q)
            answer = sorted(q, key=lambda x: x[0])[pos][0]
            break
    return answer

v= solution([3,1,2],4)
print(v)
