N, M = map(int, input().split())
data = sorted(list(map(int, input().split())))
arr = []

def btk(depth):
    if depth == M:
        print(*arr, sep=" ")
        return
    before = -1
    for i, v in enumerate(data):
        if v != before:
            before = v
            arr.append(v)
            btk(depth + 1)
            arr.pop()
btk(0)