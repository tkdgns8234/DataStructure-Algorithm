N, M = map(int, input().split())
arr = []
def btk(depth):
    if depth == M:
        print(*arr, sep=" ")
        return
    for i in range(1, N+1):
        arr.append(i)
        btk(depth + 1)
        arr.pop()

btk(0)