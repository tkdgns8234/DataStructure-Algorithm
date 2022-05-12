# 쉽다 pass
import bisect

N = int(input())
data1 = list(map(int, input().split()))
M = int(input())
data2 = list(map(int, input().split()))
data1.sort()

def find(i):
    l = bisect.bisect_left(data1, i)
    r = bisect.bisect_right(data1, i)
    return r-l

for i in data2:
    p = find(i)
    print(p, end=" ")