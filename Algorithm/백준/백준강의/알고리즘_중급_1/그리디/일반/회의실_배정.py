N = int(input())
time = []
for _ in range(N):
    time.append(list(map(int, input().split())))
time.sort(key=lambda x:(x[1], x[0]))

ans = 0
cur_end = 0
for i in range(N):
    start_time, end_time = time[i][0], time[i][1]
    if cur_end <= start_time:
        cur_end = end_time
        ans += 1
print(ans)


# 이전 코드
# 더 좋은 코드
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