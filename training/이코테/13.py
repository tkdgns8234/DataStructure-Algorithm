# 치킨거리
# N = 크기
# M = 치킨집 최대 갯수
from itertools import combinations

HOUSE = 1
CHICKEN = 2

N, M = map(int, input().split())

chicken = []
house = []

data = []
for i in range(N):
    temp = list(map(int, input().split()))
    for j, t in enumerate(temp):
        if t == HOUSE:
            house.append((i, j))
        elif t == CHICKEN:
            chicken.append((i, j))

result = int(1e9)
for comb in combinations(chicken, M):
    chicken_dist = 0
    for h in house:
        dist = int(1e9)
        for c in comb:
            dist = min(dist, abs(h[0] - c[0]) + abs(h[1] - c[1]))
        chicken_dist += dist
    result = min(result, chicken_dist)
print(result)
 