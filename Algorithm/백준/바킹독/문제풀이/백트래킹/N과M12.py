N, M = map(int, input().split())
data = sorted(list(map(int, input().split())))
arr = []
def btk(depth, start):
    if depth == M:
        print(*arr, sep=" ")
        return
    before = -1
    for i in range(start, N):
        if before != data[i]:
            before = data[i]
            arr.append(data[i])
            btk(depth+1, i)
            arr.pop()
btk(0,0)
