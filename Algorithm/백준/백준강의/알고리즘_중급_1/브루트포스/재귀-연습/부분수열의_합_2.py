from itertools import combinations

N = int(input())
numbers = list(map(int, input().split()))

possible = set()
for i in range(1, N+1):
    for comb in combinations(numbers, i):
        possible.add(sum(comb))

for i in range(1, int(1e9)):
    if i not in possible:
        print(i)
        break


# 다른 사람 풀이
# 와우,, 정말 간결하다
# iterable로 감싸면 언패킹을 할 수 있구나

input()
a=0
for i in [*sorted(map(int, input().split()))]:
    if a+1<i:break
    a+=i
print(a+1)