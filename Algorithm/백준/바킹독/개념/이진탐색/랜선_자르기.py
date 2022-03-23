# 문제4 랜선자르기
# 전형적인 이분탐색 + 파라메트릭 서치 문제
# 파라메트릭 서치: 최적화 문제 (최솟값, 최댓값을 찾는 문제) 를 결정문제로 바꾸어 푸는 것

# k : 이미가지고있는 랜선의 갯수 n: 필요한 랜선의 갯수
k, n = map(int, input().split())
data = [int(input()) for i in range(k)]

start = 1
end = max(data)
result = 0

while start <= end:
    mid = (start + end) // 2

    count = 0
    for i in data:
        count += i // mid

    if count >= n:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)