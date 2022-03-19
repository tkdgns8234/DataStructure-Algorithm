#생략
from itertools import combinations

HOUSE = 1
CHICKEN = 2
n, m = map(int, input().split())

house = []
chicken = []
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(len(data)):
        if data[j] == HOUSE:
            house.append((i, j))
        elif data[j] == CHICKEN:
            chicken.append((i, j))

comb = list(combinations(chicken, m))

result = int(1e9)
for c in comb:
    total = 0
    for h in house:
        min_val = int(1e9)
        for i in c:
            hx, hy = h
            cx, cy = i
            min_val = min(min_val, abs(hx-cx) + abs(hy-cy))
        total += min_val
    result = min(result, total)
print(result)
