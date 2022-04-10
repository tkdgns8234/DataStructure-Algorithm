# 6. 선 긋기
# O(n) 이하의 시간복잡도로 해결해야함
# 데이터를 정렬한 후
# 시작점 끝점 기준으로 시작점이 이전끝점보다 안쪽에 존재하는 경우
# 이전 데이터의 끝점을 갱신
# 아닌경우
# 신규대입
# 정렬 상태이기떄문에 n^2 시간소요되지않음
# 시간이 rstrip, sort에 따라 천지차이네?
import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)] # rstrip() 을 추가하면 시간 700~800ms 더 소요
data.sort(key=lambda x: x[0])  # data.sort() 시, 시간 1000ms 더 소요, 정렬하고자하는 데이터가 크기 때문 2개 정렬 시 O(nlogn+nlogn)

result = 0
before_start, before_end = data[0][0], data[0][1]
for i in range(1, n):
    start = data[i][0]
    end = data[i][1]

    if start <= before_end < end:
        before_end = end

    elif before_end < start:
        result += before_end - before_start
        before_end = end
        before_start = start

# 한번의 계산은 더 해야한다
result += before_end - before_start

print(result)
