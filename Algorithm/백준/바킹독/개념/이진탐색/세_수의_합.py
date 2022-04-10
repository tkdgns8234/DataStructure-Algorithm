# 문제3 세 수의 합
# 1. 1000개중 3개를 뽑는 경우의 수 -> 1000C3 으로 1억이 넘어서 안됨
# 2. N이 1000 이므로 N^2 or NlogN 으로 해결해야함
# 3. 이런 경우, 연산을 나눠서 수행하면 시간복잡도가 줄어든다
# 4. 두개의 합을 먼저 구한다(1000C2)로 n^2 시간에 수행
# 5. 나머지 하나의 수를 더해가며 이진탐색으로 찾는다 (아래 코드는 이부분 살짝 다름)
# -> N^2 + (N * NlogN)


# 시간복잡도 최적화 유형의 코드
import bisect
def find_num(arr, num):
    left = bisect.bisect_left(arr, num)
    right = bisect.bisect_right(arr, num)
    return right - left

n = int(input())
data = [int(input()) for i in range(n)]
data.sort() # 아래 for문에서 exit를 통한 최적화를 위해 추가된 코드

two = []
for i in data:
    for j in data:
        two += [i+j]
two.sort()

for i in range(len(data)-1, -1, -1):
    for j in data:
        if find_num(two, data[i] - j):
            print(data[i])
            exit(0)
