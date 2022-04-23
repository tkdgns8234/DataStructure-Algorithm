# 성공
# 파라메트릭 서치 유형으로 풀었다
# 2개의 바위를 제거 했을 때 각 지점사이의 거리 중 최솟값 중 가장 큰 값을 구해야 하는 문제인데
# 결정문제로 바꾼다
# 각 바위간 거리를 mid로 설정한다
# 시작지점부터 마지막지점까지 각 바위 사이의 거리가 mid보다 작은게 있다면 제거할 값으로 추가한다
# 제거하는경우가 좀 복잡하다 무조건 다음 값을 제거한다 (그래야 바위사이 거리가 멀어지니)
# 비교도 잘 해야한다
# 제거해야할 바위가 n개 이상이면 거리를 줄이고
# n개이하면 거리를 늘린다.

def solution(distance, rocks, n):
    rocks.append(0)
    rocks.append(distance)
    rocks.sort()

    left = 0
    right = distance
    answer = 0
    while left <= right:
        mid = (left+right)//2

        count = 0
        l, r = 0, 1
        while True:
            if l >= len(rocks) or r >= len(rocks):
                break
            if count > n:
                break
            if rocks[r] - rocks[l] < mid:
                count += 1
                r += 1
            else:
                l = r
                r = l+1

        if count > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1

    return answer

v = solution(25, [2, 14, 11, 21, 17], 2)
print(v)



# 더 좋은 코드
def solution(distance, rocks, n):
    answer = 0
    sorted_rocks = sorted(rocks)
    sorted_rocks.append(distance)
    left = 0
    right = distance
    while (left <= right):
        mid = int((left + right) / 2)
        cnt = 0
        p = 0
        for i in range(len(sorted_rocks)):
            if (sorted_rocks[i] - p < mid):
                cnt += 1
            else:
                p = sorted_rocks[i]
        if cnt > n:
            right = mid - 1
        else:
            left = mid + 1
            answer = mid
    return answer