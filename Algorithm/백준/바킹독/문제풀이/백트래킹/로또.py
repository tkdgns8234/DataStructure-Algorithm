def btk(depth, arr, start):
    global visited
    if depth == 6:
        print(" ".join(map(str, arr)))
        return
    for i in range(start, K):
        if not visited[i]:
            visited[i] = True
            arr.append(S[i])
            btk(depth + 1, arr, i+1)
            arr.pop()
            visited[i] = False

while True:
    temp = list(map(int, input().split()))
    if temp[0] == 0:
        break
    K, S = temp[0], temp[1:]
    visited = [False] * (K+1)
    arr = []
    btk(0, arr,0)
    print()