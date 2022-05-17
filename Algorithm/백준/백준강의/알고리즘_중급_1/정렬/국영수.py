N = int(input())
data = []
for _ in range(N):
    name, g, y, s = input().split()
    data.append([name,int(g) ,int(y), int(s)])

data.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))

for i in data:
    print(i[0])