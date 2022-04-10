# 문제2 회의실 배정
# 0부터 기준 시간을 설정하고 기준시간 이후의 시간 중 가장 빨리끝나는 회의를 계속 찾으면 최대의 회의를 잡을 수 있다
# 기준시간은 회의가 추가될때마다 회의의 끝시간으로 update 한다
# 정렬 시 끝시간만 정렬하는게 아니라 시작시간도 정렬해야한다
# 2,2 1,2 일 경우가 존재하기 때문
# 튜플로 정렬 시, 여러기준으로 정렬 가능

n = int(input())
meeting = [list(map(int, input().split())) for i in range(n)]
meeting.sort(key=lambda x: (x[1], x[0]))

pivot = 0
count = 0
for m in meeting:
    if pivot <= m[0]:
        count += 1
        pivot = m[1]
print(count)