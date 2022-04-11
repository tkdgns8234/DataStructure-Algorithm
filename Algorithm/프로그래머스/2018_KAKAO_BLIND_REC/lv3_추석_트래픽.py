
# 아래 3번 케이스를 생각하지 않아서 1시간동안 해맸다;;;;

# 시간이 겹칠 수 있는 케이스는 총 3가지입니다.
# 계산하는 시간 1초를 t라고 하면,
# 1. 요청시간이 t 범위에 있을 때,
# 2. 요청마감시간이 t범위에 있을 때,
# 3. 요청시간과 요청마감시간이 t범위를 감싸고 있을때 입니다.
# 2, 3, 18번케이스가 틀렸다면 3번 case를 구현하지 않으신겁니다.

def second_to_ms(time, diff):
    hour = int(time[:2])
    minute = int(time[3:5])
    second = int(time[6:8])
    ms = (hour*3600 + minute*60 + second)*1000 + int(time[9:])

    end_time = ms
    start_time = ms - int(float(diff[:-1]) * 1000) + 1
    return start_time, end_time


def solution(lines):
    times = []
    for log in lines:
        log = log.split(' ')
        start, end = second_to_ms(log[1], log[2])
        times.append((start, end))

    answer = 0
    for time in times:
        count = 0
        start, end = time[1], time[1] + 999
        for i in times:
            if start <= i[0] <= end:
                count += 1
            elif start <= i[1] <= end:
                count += 1
            elif start > i[0] and end < i[1]:  #!!!!놓쳤던 부분..
                count += 1
        answer = max(answer, count)
    return answer

v = solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"])

print(v)