# 문제4 n과 m (4)
n, m = map(int, input().split())

arr = []

def dfs(start):
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return
    for i in range(start, n + 1):
        arr.append(i)
        dfs(start + 1)
        arr.pop()
dfs(start)