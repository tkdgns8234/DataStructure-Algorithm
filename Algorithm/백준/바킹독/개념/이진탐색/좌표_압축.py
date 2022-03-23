# 문제2 좌표 압축
import copy
n = int(input())
data = list(map(int, input().split()))

tmp = copy.deepcopy(data)
tmp = list(set(tmp))
tmp.sort()

def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if tmp[mid] == target:
            return mid
        elif tmp[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

for i in data:
    print(binary_search(i, 0, len(tmp)-1), end=" ")
