# 1. 숫자 카드
# 이진탐색으로 풀었으나, set 자료구조를 활용하면 더 빠르다
import sys
import bisect
input = sys.stdin.readline

n = int(input())
data1 = list(map(int, input().split()))
m = int(input())
data2 = list(map(int, input().split()))

def binary_search(arr, target):
    left = bisect.bisect_left(arr, target)
    right = bisect.bisect_right(arr, target)
    return True if right - left > 0 else False

data1.sort()

for i in data2:
    if binary_search(data1, i):
        print(1, end=" ")
    else:
        print(0, end=" ")
