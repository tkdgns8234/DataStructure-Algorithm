#20c10 하면 20만 시간복잡도는 충분하다
from itertools import combinations,permutations
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

min_val = 1e9
for comb in list(combinations(range(N), N//2)):
    sum_1 = 0
    sum_2 = 0
    for i, j in permutations(comb, 2):
        sum_1 += arr[i][j]
    for i, j in permutations(set(range(N)) - set(comb), 2):
        sum_2 += arr[i][j]
    min_val = min(min_val, abs(sum_1-sum_2))
print(min_val)

