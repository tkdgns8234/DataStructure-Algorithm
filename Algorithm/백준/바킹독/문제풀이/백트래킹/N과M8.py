N, M = map(int, input().split())
data = sorted(list(map(int, input().split())))
arr = []
def btk(depth, start):
    if depth == M:
        print(" ".join(map(str, arr)))
        return
    for i in range(start, N):
        val = data[i]
        arr.append(val)
        btk(depth + 1, i)
        arr.pop()
btk(0, 0)