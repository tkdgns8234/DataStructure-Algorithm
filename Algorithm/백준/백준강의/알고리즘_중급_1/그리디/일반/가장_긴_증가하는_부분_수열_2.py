# 실패
# 참조: https://jason9319.tistory.com/113
import bisect

N = int(input())
data = list(map(int, input().split()))

rs = [-1]
for i in data:
    if rs[-1] < i:
        rs.append(i)
    else:
        p = bisect.bisect_left(rs, i)
        rs[p] = i
print(len(rs)-1)