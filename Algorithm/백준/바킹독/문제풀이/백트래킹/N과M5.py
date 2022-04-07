N, M = map(int, input().split())
data = list(map(int, input().split()))
arr = []
visited = [False]*(N+1)

data.sort()
def btk(depth):
    if depth == M:
        print(*arr, sep=" ")
    for i, num in enumerate(data):
        if not visited[i]:
            visited[i] = True
            arr.append(num)
            btk(depth + 1)
            arr.pop()
            visited[i] = False
btk(0)

