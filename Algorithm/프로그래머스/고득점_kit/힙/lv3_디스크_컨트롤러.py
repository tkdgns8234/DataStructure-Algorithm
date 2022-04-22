#SJF 부터 구해보자
# 왠지 답은 SRTF 일듯 싶다
# SJF네?
# 어쩐지,, SRTF는 구현 난이도가 많이 높고, 실제 알고리즘에서 구현이 불가능한 수준(오버헤드때문에)
# 처음엔 heap을 jobs 로 설정해서 해맸다.
# 처리시간을 heap으로 처리해야한다
# 그리고 jobs 를 정렬하지 않아서 한참 해맸다.
import heapq

def solution(jobs):
    jobs.sort()
    time = 0
    job_list = []
    answer = []
    while jobs or job_list:
        while jobs and jobs[0][0] <= time:
            v = jobs.pop(0)
            heapq.heappush(job_list, (v[1], v[0])) # 소요시간, 시작시간
        if job_list:
            now = heapq.heappop(job_list)
            time += now[0] # 소요시간
            answer.append(time-now[1]) # 현재시간 - 요청시간
        else:
            time += 1

    return sum(answer)//len(answer)


v = solution([[0, 10], [4, 10], [15, 2], [5, 11]])
print(v)