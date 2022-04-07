N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
arr = []
def btk(depth, start):
    if depth == M:
        print(*arr, sep=" ")
        return
    for i in range(start, N):
        val = data[i]
        arr.append(val)
        btk(depth + 1, i+1)
        arr.pop()
btk(0, 0)