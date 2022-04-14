# 09:00 부터 인원수만큼 탑승시켜야한다
# 승객을 양방향 queue 형태로 만들고 버스가 도착할때마다 pop한다
# 가장 나중에 탑승해야 하기 떄문에 마지막 배차 시간만 확인하면됨
# 마지막 배차 시간을 기준으로 자리가 없으면 마지막 탑승객 -1 시간에 탑승
# 마지막 배차 시간 기준으로 자리가 남으면 마지막 시간 탑승

from collections import deque
def solution(n, t, m, timetable):
    time = deque(sorted([int(i[:2]) * 60 + int(i[3:]) for i in timetable]))
    start_time = 540

    last_person = 0
    for bus in range(start_time, start_time+t*n, t):
        ride_person = m
        for _ in range(len(time)):
            if time[0] <= bus and ride_person > 0:
                last_person = time.popleft()
                ride_person -= 1
            else:
                break

    # 마지막 탑승시간에 남은 자리만 계산하면 됨 가장 늦게 타야하니까
    if ride_person > 0:
        # 마지막 버스 시간에 타면 됨
        answer = 540 + (n - 1) * t
    else:
        # 자리가 없는 경우
        answer = last_person - 1 # 가장 마지막에 탄 사람 -1분

    return str(answer//60).rjust(2, '0') + ':' + str(answer%60).rjust(2, '0')

print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
