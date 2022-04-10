# 2. 차집합
# set 자료구조 + 언패킹 이용
# set 자료구조의 - 연산 사용해도 됨
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
data1 = list(map(int, input().split()))
data2 = set(map(int, input().split()))

data1.sort()
result = []
for i in data1:
    if i not in data2:
        result.append(i)

print(len(result))
if len(result) > 0:
    print(*result)
