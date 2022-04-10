# 합이 0인 네 정수
# ab, cd 합 모든경우 두개 다 구해서 이진탐색으로 찾는경우 n^2 * logn 인데, 시간 초과 느낌인데
# 투포인터도 n^3 풀이밖에 안보이네
# 두 개의 리스트로 나눈 후 dict 이용해 풀어야하는듯
# 시간복잡도: O(n^2)
import sys
input = sys.stdin.readline
N = int(input())
d1, d2, d3, d4 = [], [], [], []

for _ in range(N):
    data = list(map(int, input().split()))
    d1.append(data[0]), d2.append(data[1]), d3.append(data[2]), d4.append(data[3])

ab_dict = {}
for i in d1:
    for j in d2:
        ab_dict[i+j] = ab_dict.get(i+j, 0) + 1

ans = 0
for i in d3:
    for j in d4:
            ans += ab_dict.get(-(i+j), 0)

print(ans)