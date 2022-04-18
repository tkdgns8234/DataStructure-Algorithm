# 실패

# import bisect
# import sys
#
# def time_to_second(time):
#     hour, minute, second = map(int, time.split(':'))
#     return hour*3600 + minute*60 + second
#
# def solution(play_time, adv_time, logs):
#     if play_time == adv_time:
#         return "00:00:00"
#     play_time = time_to_second(play_time)
#     adv_time = time_to_second(adv_time)
#
#     log_time = []
#     for log in logs:
#         s, e = log.split('-')
#         log_time.append((time_to_second(s), time_to_second(e)))
#
#     sorted_by_start_time = sorted(log_time, key=lambda x: x[0])
#     sorted_by_end_time = sorted(log_time, key=lambda x: x[1])
#
#
#     answer = 0
#     answer_t = 0
#     for s, e in sorted_by_start_time:
#         adv_s, adv_e = s, s+adv_time
#         # 광고 시작시간보다 시청 종료시간이 뒤이고
#         idx = bisect.bisect_left(sorted_by_end_time, (adv_s, 0))
#         temp = sorted_by_start_time[idx:]
#         # 광고 종료시간보다 시청 시작시간보다 앞인 경우
#         idx = bisect.bisect_right(sorted_by_start_time, (adv_e, sys.maxsize))
#         temp = temp[:idx]
#
#         # 겹치는 시간을 확인
#         time = 0
#         pivot_s, pivot_e = 0, 0
#         for t_s, t_e in temp:
#             if adv_s > t_s:
#                 pivot_s = adv_s
#             else:
#                 pivot_s = t_s
#             if adv_e < t_e:
#                 pivot_e = adv_e
#             else:
#                 pivot_e = t_e
#             # 겹치는 시간
#             time += (pivot_e - pivot_s)
#
#         if time > answer_t:
#             answer_t = time
#             answer = adv_s
#     hour = answer//3600
#     minute = answer//60 - hour*60
#     second = answer%60
#     return str(hour).rjust(2, '0') + ":" + str(minute).rjust(2, '0') + ":" + str(second).rjust(2, '0')
#
#
# v = solution("02:03:55",	"00:14:15",	["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])
# print(v)


# 접근방식자체가틀림,
# logs 의 길이가 30만이라고 했을 때 dp나 누적합 등 다른 방식을 떠올려야했어.
# 문제를 푸는 시간보다는 문제를 고민하고 해결방법을 찾는데 더 시간을 쏟도록 하자

# 문제 난이도가 괴랄하네; 아래는 올바른 풀이
# 시청자 수의 누적합 + dp + 발상의 전환(누적 재생시간을 기준으로 하는게 아니라 시간대별 누적 시청자 수를 통해 정답을 도출)
# https://dev-note-97.tistory.com/156#%-C%EB%AC%B-%EC%A-%-C%--%EC%--%A-%EB%AA%--%-E
def solution(play_time, adv_time, logs):
    play_time = str_to_int(play_time)        # 1
    adv_time = str_to_int(adv_time)
    all_time = [0 for i in range(play_time + 1)] # platime 은 최대 100:00:00 ->36만 -> 크기 적절 1MB 도 안됨

    for l in logs:                           # 2
        start, end = l.split('-')
        start = str_to_int(start)
        end = str_to_int(end)
        # 각 구간별 start -> 시청인원 1 증가 end -> 시청인원 -1
        all_time[start] += 1
        all_time[end] -= 1

    for i in range(1, len(all_time)):       # 3
        # 모든 구간의 (초당) 시청인원을 구함 //이전에 start, end만 기록했기 때문
        all_time[i] = all_time[i] + all_time[i - 1]

    for i in range(1, len(all_time)):       # 4
        # 모든 구간의 시청인원의 누적 합을 구함
        all_time[i] = all_time[i] + all_time[i - 1]

    most_view = 0                           # 5
    max_time = 0
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < all_time[i] - all_time[i - adv_time]:
                most_view = all_time[i] - all_time[i - adv_time]
                max_time = i - adv_time + 1
        else:
            # adv_time == playtime 인 경우를 위해
            if most_view < all_time[i]:
                most_view = all_time[i]
                max_time = i - adv_time + 1

    return int_to_str(max_time)


def str_to_int(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def int_to_str(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s


