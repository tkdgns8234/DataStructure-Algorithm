N = int(input())
data = []
for _ in range(N):
    a, b = map(int, input().split())
    data.append([a, b])
data.sort(key=lambda x:(x[0], x[1]))

for a, b in data:
    print(a, b)