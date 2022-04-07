N, M = map(int, input().split())
data = sorted(list(map(int, input().split())))
arr = []
visited = [False]*(N+1)
def btk(depth):
    if depth == M:
        print(" ".join(map(str, arr)))
        return
    overlap = 0
    for i, v in enumerate(data):
        if not visited[i] and v != overlap:
            overlap = v
            visited[i] = True
            arr.append(v)
            btk(depth + 1)
            arr.pop()
            visited[i] = False
btk(0)
