N, M = map(int, input().split())
arr = []
def btk(depth, start):
    if depth == M:
        print(*arr, sep=" ")
    for i in range(start, N+1):
        arr.append(i)
        btk(depth + 1, i + 1)
        arr.pop()

btk(0, 1)
