# 이미 푼 문제, 다시풀자

# 아래 지문은 큐의 성질 FIFO

#또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고,
# 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

# 남은 days를 기준으로 pop

import math
from collections import deque


def solution(progresses, speeds):
    remain_days = deque()
    for i in range(len(progresses)):
        remain_days.append(math.ceil((100-progresses[i])/speeds[i]))

    answer = []
    while remain_days:
        now = remain_days.popleft()
        count = 1
        while remain_days and remain_days[0] <= now:
            remain_days.popleft()
            count += 1
        answer.append(count)

    return answer

v= solution([95, 90, 99, 99, 80, 99]	,[1, 1, 1, 1, 1, 1]	)
print(v)