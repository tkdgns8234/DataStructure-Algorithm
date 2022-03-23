# 문제3 세 수의 합
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
