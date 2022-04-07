N, M = map(int, input().split())
data = sorted(list(map(int, input().split())))
arr = []
visited = [False]*(N+1)
def btk(depth, start):
    if depth == M:
        print(" ".join(map(str, arr)))
        return
    before = 0
    for i in range(start, N):
        if not visited[i] and before != data[i]:
            before = data[i]
            visited[i] = True
            arr.append(data[i])
            btk(depth+1, i+1)
            visited[i] = False
            arr.pop()
btk(0, 0)
