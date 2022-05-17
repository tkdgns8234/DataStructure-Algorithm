# 파라메트릭 서치
import sys


def parametric_search(start, end):
    global ans
    while start<=end:
        mid = (start+end)//2

        pivot = -sys.maxsize
        cnt = 0
        for d in data:
            if d-pivot >= mid:
                cnt += 1
                pivot = d

        if cnt >= C:
            ans = max(mid, ans)
            start = mid + 1
        else:
            end = mid - 1

N, C = map(int, input().split())
data = sorted([int(input()) for _ in range(N)])
ans = 0
parametric_search(0, max(data))
print(ans)