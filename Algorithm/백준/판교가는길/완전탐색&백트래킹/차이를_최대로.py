#n 이 매우 작은 수 이기때문에 완전탐색
from itertools import permutations
N = int(input())
L = map(int, input().split())
ans = 0
for l in list(permutations(L, N)):
    sum_ = 0
    for i in range(N-1):
        sum_ += abs(l[i] - l[i + 1])
    ans = max(ans, sum_)
print(ans)