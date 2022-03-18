from itertools import combinations
N, M = map(int, input().split())
L = list(map(int, input().split()))

ans = 0
for comb in combinations(L, 3):
    sum_ = sum(comb)
    if sum_ <= M:
        ans = max(ans, sum_)
print(ans)
