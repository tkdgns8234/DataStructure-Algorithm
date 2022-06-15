from collections import Counter

N = int(input())
data = list(map(int, input().split()))
counter = Counter(data)

answer = [-1]*N
stack = [0]
for i, d in enumerate(data):
    while stack and counter[data[stack[-1]]] < counter[d]:
        now = stack[-1]
        answer[now] = d
        stack.pop()
    stack.append(i)

print(*answer)