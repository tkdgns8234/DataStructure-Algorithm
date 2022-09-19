from itertools import combinations

n, m = map(int, input().split())
data = list(map(int, input().split()))

total = len(list(combinations(data, 2)))

# 중복되는 숫자의 갯수 구하기
cnt = [0 for _ in range(10)]
for i in data:
    cnt[int(i)] += 1

# 중복제거
for i in cnt:
    if i >= 2:
        total -= len(list(combinations([k for k in range(i)], 2)))

print(total)