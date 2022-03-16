def solution(a, b):
    today = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    m_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0
    for i in range(a-1):
        day += m_days[i]
    day = day + b

    answer = today[day % 7 - 1]
    return answer