# 박수가 나오는 문제다..
# 이분탐색 응용 문제
# 자세한 풀이를 참고했다
# 다시풀자
# https://studyposting.tistory.com/65


# 구간 점수의 최댓값중 최솟값을 만족하는 M 개 이하의 구간을 찾기
# 구간이 적으면 최댓값중 최솟값을 낮추기

def split_array(mid):
    cnt = 1
    min_val, max_val = int(1e9), -int(1e9)
    for i in range(len(data)):
        min_val, max_val = min(min_val, data[i]), max(max_val, data[i])
        if max_val-min_val > mid:
            cnt += 1
            min_val, max_val = data[i], data[i]
    return cnt


N, M = map(int, input().split())
data = list(map(int, input().split()))

ans = int(1e9)
start, end = 0, 10000
while start <= end:
    mid = (start+end)//2
    cnt = split_array(mid)

    if cnt <= M:
        ans = min(ans, mid)
        end = mid - 1
    else:
        start = mid + 1

print(ans)