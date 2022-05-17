N = int(input())
data = []
for _ in range(N):
    age, name = input().split()
    data.append([int(age), name])
data.sort(key=lambda x:x[0])
for a,d in data:
    print(a, d)
