# 파라메트릭 서치
# 거리 = logn 10억
# 집의 갯수 20만

# 거리 ? 로 했을 때  C 개의 공유기 설치 가능한지 확인
N, C = map(int, input().split())
data = sorted([int(input()) for _ in range(N)])
max_pos = max(data)

start = 0
end = max_pos
result = 0
while start <= end:
    mid = (start + end) // 2

    prev_pos = 0
    count = 1

    for i in range(1, len(data)):
        if data[i] - data[prev_pos] >= mid:
            count += 1
            prev_pos = i

    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)