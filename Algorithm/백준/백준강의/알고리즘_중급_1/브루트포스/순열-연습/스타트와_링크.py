# 이미 푼 문제
# 해결 방법만 떠올리고 skip
# 브루트포스
# combination으로 팀을 뽑으면 쉬울거같은데?
# 시간복잡도도 충분 20C10

# -- 이전 코드를 본 후 --
# 스타트, 링크팀 분리 후 각 팀의 능력치를 구할 때, set, permu를 사용하네 좋은 코드다
# 잘 살펴보자

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


