# 이코테 문제풀이
# 1
import sys

input = sys.stdin.readline
n = input()
data = sorted(map(int, input().split()))

result = 0
group = []
for i in data:
    group.append(i)
    if i == len(group):
        result += 1
        group.clear()

print(result)