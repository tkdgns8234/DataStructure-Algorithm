
# 더 나은코드가 아래에 있음
import bisect
import sys
input = sys.stdin.readline
D, N = map(int, input().split())

oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))

# 각각의 피자가 들어갈 수 있는 크기로 변환
new_oven = []

v = int(1e9)
for i in range(D):
    v = min(v, oven[i])
    new_oven.append(v)

new_oven.sort()
start, end = 0, D
ans = 0
for i in range(N):
    index = bisect.bisect_left(new_oven, pizza[i], lo=start)
    if index == end:
        print(0)
        exit()
    start = index + 1
    ans += (start - ans)

print(D-ans+1)


# [파이썬 | BOJ | 1756] 피자 굽기

import sys

read = sys.stdin.readline
inf = sys.maxsize

D, N = map(int, read().split())
oven = list(map(int, read().split()))
pizza = list(map(int, read().split()))

for i in range(1, D):
    oven[i] = min(oven[i], oven[i - 1])

pizzaIdx = 0
depth = D - 1
for i in reversed(range(D)):
    if pizzaIdx >= len(pizza):
        print(depth + 1)
        sys.exit(0)

    if oven[i] >= pizza[pizzaIdx]:
        pizzaIdx += 1
        depth = i

print(0)