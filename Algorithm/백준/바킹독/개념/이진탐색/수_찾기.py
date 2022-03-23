# 문제1 수 찾기
# 가장 기본적인 이진탐색
# 이진탐색 전 정렬을 수행
# 파이썬의 bisect_left, right 라이브러리의 경우 데이터가 없는 경우 0 을 리턴함
import bisect
n = int(input())
data = list(map(int, input().split()))
m = int(input())
pivot = list(map(int, input().split()))

def find_num(num):
    left = bisect.bisect_left(data, num)
    right = bisect.bisect_right(data, num)
    return True if right - left > 0 else False

data.sort()
for i in pivot:
    if find_num(i):
        print(1)
    else:
        print(0)