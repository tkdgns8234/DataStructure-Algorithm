N, M = map(int, input().split())
data = list(map(int, input().split()))
arr = []

data.sort()
def btk(depth):
    if depth == M:
        print(*arr, sep=" ")
        return
    for i in data:
        arr.append(i)
        btk(depth + 1)
        arr.pop()
btk(0)